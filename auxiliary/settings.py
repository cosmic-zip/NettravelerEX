from auxiliary.interface.web.generator import gen_wrapper
from auxiliary.modules.genreport.reporter import gen_report_wrapper
from auxiliary.modules.osint.keyword_scanner import keyword_scanner_wrapper
from auxiliary.modules.scanner.dns import scanner_dns
from auxiliary.modules.scanner.ip_score import scanner_ip_score_addr
from auxiliary.modules.scanner.nmapper import nmapper
from auxiliary.modules.server.server import server_wrapper, server_llama_wrapper, server_default_wrapper

FN_REGISTRY = {
    "scanner.keyword": keyword_scanner_wrapper,
    "scanner.dns": scanner_dns,
    "scanner.ip": scanner_ip_score_addr,
    "scanner.nmapper": nmapper,
    "server": server_wrapper,
    "server.yuri": server_llama_wrapper,
    "server.default": server_default_wrapper,
    "build.web": gen_wrapper,
    "gen.report": gen_report_wrapper,
}
