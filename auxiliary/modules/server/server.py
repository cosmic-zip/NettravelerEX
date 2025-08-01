import os
from auxiliary.netlibpy.netlib import *


def llama_api_server(host: str, port: int) -> int:
    command = (
        f"cd {DATAROOT}/bin/llama/ && "
        f"./llama-server --port {port} "
        f"-m ../../models/Llama-3.2-3B-Instruct-uncensored-Q4_K_S.gguf"
    )
    net_logger("llama server is running!", color="yellow", style="bold", newline=True)

    buffer = net_exec(command)

    if buffer is None:
        net_logger("llama server failed to start", color="yellow", style="bold", newline=True)
        net_logger(str(buffer), color="white", style="normal", newline=True)

    return 0

def server(host: str, port: str, folder: str, ztoken: str, full: str) -> int:

    if full == "yes":
        os.system(f"./nettraveler.py server.yuri --host {host} --port 5599 &")

    net_logger(f"Running web server! http://{host}:{port}", "green", "bold", True)
    command = f"{DATAROOT}bin/server/server {host} {port} {folder} {ztoken}"
    buffer = net_exec(command)["stdout"]
    net_logger(buffer, "white", "normal", True)

    return 0

def server_llama_wrapper(args_v):
    host = search_arg(args_v, "host")
    port = search_arg(args_v, "port")
    return  llama_api_server(host, port) 

def server_default_wrapper(args_v):
    ztoken = COSMIC_SIGKEY
    return server("localhost", "5500", f"{DATAROOT}webui", ztoken, "yes")

def server_wrapper(args_v):
    host = search_arg(args_v, "host")
    port = search_arg(args_v, "port")
    folder = search_arg(args_v, "folder")
    full = search_arg(args_v, "full", False)
    ztoken = COSMIC_SIGKEY
    return server(host, port, folder, ztoken, full)

