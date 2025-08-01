from auxiliary.netlibpy.netlib import *

def scanner_dns(args_v):
    domain = search_arg(args_v, "domain")

    net_logger("[scanner_dns] :: Scanning dns records at: " + domain, "cyan", "bold")

    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SOA", "SRV", "PTR", "DNSKEY"]
    for rec in record_types:
        cmd = ("dig @@domain " + rec + " +short").replace("@@domain", domain)
        text = net_exec(cmd).get('stdout')
        text = text.replace(";", " ")
        net_logger("Record type: " + rec, "cyan", "bold")
        net_logger(text, "white")

    cmds = [
        ["whois", "whois @@domain"],
        ["robots", "curl -sS -L https://@@domain/robots.txt"],
        ["sitemap", "curl -sS -L https://@@domain/sitemap.xml"]
    ]

    for entry in cmds:
        name = entry[0]
        cmd = entry[1].replace("@@domain", domain)
        text = net_exec(cmd).get('stdout')
        net_logger("Running a extra scanning :: " + name, "cyan", "bold", True)
        net_logger(text, "white")

    databases = [
        ["fakenews", DATAROOT + "osint/dns/fakenews.hosts"],
        ["gambling", DATAROOT + "osint/dns/gambling.hosts"],
        ["malware", DATAROOT + "osint/dns/malware.hosts"],
        ["porn",     DATAROOT + "osint/dns/porn.hosts"],
        ["social",   DATAROOT + "osint/dns/social.hosts"]
    ]

    net_logger("Trying lookup DNS category", "cyan", "bold")
    for entry in databases:
        label = entry[0]
        path  = entry[1]
        net_logger("Searching in the list of: " + label, "cyan", "bold")

        buffer = ""
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                for line in file:
                    if domain in line:
                        buffer += line
        except:
            continue

        if buffer:
            net_logger(buffer.replace("0.0.0.0 ", "\t"), "green", "bold")

    return 0
