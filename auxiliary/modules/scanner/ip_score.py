import os
import ipaddress
from auxiliary.netlibpy.netlib import *

def scanner_ip_score_addr(args_v: str) -> int:
    ip_addr = search_arg(args_v, "ip")

    try:
        target_ip = ipaddress.ip_address(ip_addr)
        target_ip_int = int(target_ip)
    except ValueError:
        net_logger(f"Invalid IP address: {ip_addr}", "red", "bold", True)
        return 1

    databases = {
        "ans": os.path.join(DATAROOT, "osint/ip/ans.csv"),
        "proxy": os.path.join(DATAROOT, "osint/ip/proxy.csv"),
        "geoloc": os.path.join(DATAROOT, "osint/ip/geoloc.csv"),
        "cibadguys": os.path.join(DATAROOT, "osint/ip/ci-badguys.txt"),
        "geoloc_fallback": os.path.join(DATAROOT, "osint/ip/geoloc_lite.csv"),
    }

    net_logger("[scanner_ip] :: Search for more IP info!", "cyan", "bold", True)

    for name, path in databases.items():
        net_logger(f"Trying database :: {name}", "white", "bold")

        if not os.path.exists(path):
            net_logger(f"File not found: {path}", "red", "normal", True)
            continue

        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                for lineno, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue

                    if ip_addr in line:
                        net_logger(f"Found IP string match in {name} at line {lineno}: {line}", "green", "bold", True)
                        break

                    try:
                        line_int = int(line)
                        if line_int == target_ip_int:
                            net_logger(f"Found IP integer match in {name} at line {lineno}: {line}", "green", "bold", True)
                            break
                    except ValueError:
                        pass
        except Exception as e:
            net_logger(f"Error reading {path}: {e}", "red", "normal", True)

    return 0

