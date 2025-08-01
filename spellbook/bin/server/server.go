package main

import (
	"context"
	"errors"
	"fmt"
	"io"
	"log"
	"net/http"
	"net/url"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"time"
	"syscall"
)

type Server struct {
	Folder string
	Token  string
	Logger *log.Logger
}

func (s *Server) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		s.serveFile(w, r)
	case http.MethodPost:
		s.handleExec(w, r)
	default:
		http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
	}
}

func (s *Server) serveFile(w http.ResponseWriter, r *http.Request) {
	cleanPath := filepath.Clean(r.URL.Path)
	if cleanPath == "/" {
		cleanPath = "/index.html"
	}

	fullPath := filepath.Join(s.Folder, cleanPath)
	data, err := os.ReadFile(fullPath)
	if err != nil {
		http.Error(w, "404 Not Found", http.StatusNotFound)
		return
	}

	contentType := mimeType(fullPath)
	w.Header().Set("Content-Type", contentType)
	w.WriteHeader(http.StatusOK)
	w.Write(data)
}

func (s *Server) handleExec(w http.ResponseWriter, r *http.Request) {
	defer r.Body.Close()

	body, err := io.ReadAll(io.LimitReader(r.Body, 8192))
	if err != nil || len(body) == 0 {
		http.Error(w, "Invalid Request", http.StatusBadRequest)
		return
	}

	formData, err := url.ParseQuery(string(body))
	if err != nil {
		http.Error(w, "Invalid Form Encoding", http.StatusBadRequest)
		return
	}

	clientToken := formData.Get("ztoken")
	if clientToken != s.Token {
		http.Error(w, "Unauthorized", http.StatusUnauthorized)
		return
	}

	cmdline, err := buildCommand(formData)
	if err != nil {
		http.Error(w, "Bad Request: "+err.Error(), http.StatusBadRequest)
		return
	}

	s.logRequest(string(body))

	ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
	defer cancel()

	cmd := exec.CommandContext(ctx, "./nettraveler.py", append(cmdline, "--output_mode_html")...)
	output, err := cmd.CombinedOutput()
	
	if err != nil {
		// Always return script output to caller
		w.WriteHeader(http.StatusInternalServerError)

		// Check if exit status is exactly 2
		exitMessage := ""
		if exitErr, ok := err.(*exec.ExitError); ok {
			if status, ok := exitErr.Sys().(syscall.WaitStatus); ok && status.ExitStatus() == 2 {
				exitMessage = "\n[Notice] nettraveler.py exited with status code 2: possible misuse, bad CLI args or internal parser error."
			}
		}

		// Print error + output + diagnostic message (if any)
		fmt.Fprintf(w, "Exec Error: %v\n%s%s", err, cmdline, exitMessage)
		return
	}

	w.WriteHeader(http.StatusOK)
	w.Write(output)
}

func buildCommand(values url.Values) ([]string, error) {
	var args []string

	for k := range values {
		if strings.Contains(k, "EZEC") {
			k = strings.ReplaceAll(k, "_", ".")
			k = strings.ReplaceAll(k, "EZEC", "")
			k = strings.ReplaceAll(k, "native.", "")
			k = filterAlpha(k)
			if k != "" {
				args = append(args, k)
			}
		}
	}

	for k, v := range values {
		if k == "ztoken" || strings.Contains(k, "EZEC") || k == "requestid" {
			continue
		}
		flag := filterAlpha(k)
		if flag == "" || len(v) == 0 {
			continue
		}
		val := strings.ReplaceAll(v[0], "%2F", "/")
		args = append(args, "--"+flag, val)
	}

	if len(args) == 0 {
		return nil, errors.New("no command arguments constructed")
	}

	return args, nil
}

func filterAlpha(s string) string {
	var out strings.Builder
	for _, c := range s {
		if c >= 'a' && c <= 'z' || c == '.' || c == '-' || c == '_' {
			out.WriteRune(c)
		}
	}
	return out.String()
}

func mimeType(path string) string {
	switch filepath.Ext(path) {
	case ".html", ".htm":
		return "text/html"
	case ".css":
		return "text/css"
	case ".js":
		return "application/javascript"
	case ".jpg", ".jpeg":
		return "image/jpeg"
	case ".png":
		return "image/png"
	case ".gif":
		return "image/gif"
	case ".svg":
		return "image/svg+xml"
	case ".txt":
		return "text/plain"
	default:
		return "application/octet-stream"
	}
}

func (s *Server) logRequest(raw string) {
	if s.Logger == nil {
		return
	}
	clean := strings.ReplaceAll(raw, "\x00", "")
	s.Logger.Println(clean)
}

func main() {
	if len(os.Args) != 5 {
		fmt.Fprintf(os.Stderr, "Usage: %s <host> <port> <folder> <ztoken>\n", os.Args[0])
		os.Exit(1)
	}

	host := os.Args[1]
	port := os.Args[2]
	folder := os.Args[3]
	ztoken := os.Args[4]

	if stat, err := os.Stat(folder); err != nil || !stat.IsDir() {
		fmt.Fprintf(os.Stderr, "Error: Folder '%s' does not exist or is not a directory\n", folder)
		os.Exit(1)
	}

	logFile, err := os.OpenFile("evil_server.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println("Logger failed:", err)
		os.Exit(1)
	}
	defer logFile.Close()

	srv := &Server{
		Folder: folder,
		Token:  ztoken,
		Logger: log.New(logFile, "", log.LstdFlags),
	}

	addr := fmt.Sprintf("%s:%s", host, port)
	fmt.Printf("Server running on http://%s serving %s\n", addr, folder)
	err = http.ListenAndServe(addr, srv)
	if err != nil {
		log.Fatalf("Server failed: %v", err)
	}
}
