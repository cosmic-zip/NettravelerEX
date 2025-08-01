from auxiliary.netlibpy.netlib import *
import json


def gen_auto_owasp(lang: str, attacks_list=[], vulns_list=[], enable_output=True):

    def print_auto_owasp_list(json_obj_list, enable_output: bool):
        if enable_output:
            for obj in json_obj_list:
                net_logger(f"\t{obj.get('id')}")
                net_logger(f"\t{obj.get('name')}")
                net_logger(f"\t{obj.get('description')}")
                net_logger(f"\t{obj.get('mitigation')}")
                net_logger(f"\t{obj.get('severity_score')}")
                net_logger(f"\t{obj.get('severity_level')}")

    attacks = None
    vulns = None

    if lang in ["en", "us"]:
        with open(f"{DATAROOT}reporter/auto_owasp/vulns_en.json") as file:
            vulns = json.load(file).get("index")
        with open(f"{DATAROOT}reporter/auto_owasp/attacks_en.json") as file:
            attacks = json.load(file).get("index")

    if lang in ["pt", "pt-br", "br"]:
        with open(f"{DATAROOT}reporter/auto_owasp/vulns_br.json") as file:
            vulns = json.load(file).get("index")
        with open(f"{DATAROOT}reporter/auto_owasp/attacks_br.json") as file:
            attacks = json.load(file).get("index")

    if attacks_list is None and vulns_list is None:
        eyeliner("List of OWASP attacks")
        print_auto_owasp_list(attacks)
        eyeliner("List of OWASP vulnerabilities")
        print_auto_owasp_list(vulns)

    template = """
    id: @@id
    name: @@name
    description: @@description
    mitigation: @@mitigation
    severity_score: @@severity_score
    severity_level: @@severity_level

    """

    def fn_template_build(js_list, compare_list):
        if js_list:
            nv_template = ""
            for obj in js_list:
                if int(obj.get("id")) in compare_list:
                    buff = (
                        template.replace("@@id", str(obj.get("id")))
                        .replace("@@name", obj.get("name"))
                        .replace("@@description", obj.get("description"))
                        .replace("@@mitigation", obj.get("mitigation"))
                        .replace("@@severity_score", str(obj.get("severity_score")))
                        .replace("@@severity_level", str(obj.get("severity_level")))
                    )
                    nv_template = nv_template + buff
            return nv_template

    if len(attacks_list) > 0:
        return fn_template_build(attacks, attacks_list)
    if len(vulns_list) > 0:
        return fn_template_build(vulns, vulns_list)

    return " "


def gen_report(
    title: str,
    lang: str,
    sginature: str,
    sys_type: str,
    target: str,
    tech_stack: str,
    date: str,
    vulnerabilities: str,
    vectors: str,
    fixes: str,
    final_notes: str,
):

    markdown = None
    if lang in ["en", "us"]:
        with open(f"{DATAROOT}reporter/templates/cosmic_report_template_en.md") as file:
            markdown = file.read()

    if lang in ["pt", "pt-br", "br"]:
        with open(f"{DATAROOT}reporter/templates/cosmic_report_template_br.md") as file:
            markdown = file.read()

    if markdown is None:
        net_logger("[error] :: A invalid language has been select")

    output = (
        markdown.replace("@@TITLE", title)
        .replace("@@SGINATURE", sginature)
        .replace("@@SYS_TYPE", sys_type)
        .replace("@@TARGET", target)
        .replace("@@TECH_STACK", tech_stack)
        .replace("@@DATE", date)
        .replace(
            "@@VULNERABILITIES",
            gen_auto_owasp(lang, vulns_list=list(vulnerabilities), enable_output=False),
        )
        .replace(
            "@@VECTORS",
            gen_auto_owasp(lang, attacks_list=list(vectors), enable_output=False),
        )
        .replace("@@FIXES", fixes)
        .replace("@@FINAL_NOTES", final_notes)
    )

    return output


def gen_report_wrapper(args_v) -> int:
    title = search_arg(args_v, "title")
    lang = search_arg(args_v, "lang")
    sginature = search_arg(args_v, "sginature")
    sys_type = search_arg(args_v, "sys_type")
    target = search_arg(args_v, "target")
    tech_stack = search_arg(args_v, "tech_stack")
    date = search_arg(args_v, "date")
    vulnerabilities = search_arg(args_v, "vulnerabilities")
    vectors = search_arg(args_v, "vectors")
    fixes = search_arg(args_v, "fixes")
    final_notes = search_arg(args_v, "final_notes")

    print(
        gen_report(
            title,
            lang,
            sginature,
            sys_type,
            target,
            tech_stack,
            date,
            vulnerabilities,
            vectors,
            fixes,
            final_notes,
        )
    )

    return 0