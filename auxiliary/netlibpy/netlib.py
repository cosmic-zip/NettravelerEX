#!/usr/bin/env python3

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#                                                                                                                               #
#       Netlib is a library for the NettravalerEX orginaly written in Lua, the main parts of the code base has been             #
#       rewritten in python for the convenience of find new contributor and employes for the comsic Sec&Dev company.            #
#                                                                                                                               #
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
import sys, os, json, subprocess

VERSION = "NetTravelerEX Minimal v0.0.99 by COSMIC ZIP 11-APR-2025"
DATAROOT = os.getenv("NT_DATAROOT", "spellbook/") 
SETUP_COLORS = "color"  # none color html
ENABLE_LOGGER = False
ENABLE_ARBITRARY_SHELL = True
SESSION = "default"
COSMIC_SIGKEY = "b7a5f1f46944d5cc438646c547e20b177257608b5dfff41d7c5f063a6ea092fe"
GEN_HOST = "http://localhost:5500"
GEN_TITLE = "⛩️ NettravalerEX"
HEADLESS_BROWSER_BIN = "chromium"

BANNER = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                            NetTravelerEX Minimal v0.0.99 by COSMIC ZIP 11-APR-2025
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 
                ███╗   ██╗███████╗████████╗████████╗██████╗  █████╗ ██╗   ██╗███████╗██╗     ███████╗██████╗ 
                ████╗  ██║██╔════╝╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║   ██║██╔════╝██║     ██╔════╝██╔══██╗
                ██╔██╗ ██║█████╗     ██║      ██║   ██████╔╝███████║██║   ██║█████╗  ██║     █████╗  ██████╔╝
                ██║╚██╗██║██╔══╝     ██║      ██║   ██╔══██╗██╔══██║╚██╗ ██╔╝██╔══╝  ██║     ██╔══╝  ██╔══██╗
                ██║ ╚████║███████╗   ██║      ██║   ██║  ██║██║  ██║ ╚████╔╝ ███████╗███████╗███████╗██║  ██║
                ╚═╝  ╚═══╝╚══════╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 
CORES                            What it does
 
BINDS                            A series os shell script that runs common tasks
ARBITRARY                        Run a arbitrary command if a bind, native function or scheduler arn't found
 
MODES
 
SHELL                            Run like a shell command
INTERACTIVE                      Run with a friendly assistant (BETA)
 
HELP                             Run: nettraveler help or manual 
 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""

PROGRESS_BAR = [
    "█▒▒▒▒▒▒▒▒▒ 10% ",
    "██▒▒▒▒▒▒▒▒ 20% ",
    "███▒▒▒▒▒▒▒ 30% ",
    "████▒▒▒▒▒▒ 40% ",
    "█████▒▒▒▒▒ 50% ",
    "██████▒▒▒▒ 60% ",
    "███████▒▒▒ 70% ",
    "████████▒▒ 80% ",
    "█████████▒ 90% ",
    "██████████ 100%",
]

COLORS = {
    # Basic colors
    "black": "\033[30m@@\033[0m",
    "red": "\033[31m@@\033[0m",
    "green": "\033[32m@@\033[0m",
    "yellow": "\033[33m@@\033[0m",
    "blue": "\033[34m@@\033[0m",
    "magenta": "\033[35m@@\033[0m",
    "cyan": "\033[36m@@\033[0m",
    "white": "\033[37m@@\033[0m",
    # Bright colors
    "bright_black": "\033[90m@@\033[0m",
    "bright_red": "\033[91m@@\033[0m",
    "bright_green": "\033[92m@@\033[0m",
    "bright_yellow": "\033[93m@@\033[0m",
    "bright_blue": "\033[94m@@\033[0m",
    "bright_magenta": "\033[95m@@\033[0m",
    "bright_cyan": "\033[96m@@\033[0m",
    "bright_white": "\033[97m@@\033[0m",
    # Background colors
    "bg_black": "\033[40m@@\033[0m",
    "bg_red": "\033[41m@@\033[0m",
    "bg_green": "\033[42m@@\033[0m",
    "bg_yellow": "\033[43m@@\033[0m",
    "bg_blue": "\033[44m@@\033[0m",
    "bg_magenta": "\033[45m@@\033[0m",
    "bg_cyan": "\033[46m@@\033[0m",
    "bg_white": "\033[47m@@\033[0m",
    # Styles
    "bold": "\033[1m@@\033[0m",
    "dim": "\033[2m@@\033[0m",
    "italic": "\033[3m@@\033[0m",
    "underline": "\033[4m@@\033[0m",
    "blink": "\033[5m@@\033[0m",
    "reverse": "\033[7m@@\033[0m",
    "hidden": "\033[8m@@\033[0m",
    "strike": "\033[9m@@\033[0m",
    "normal": "@@",
}

COLORS_HTML = {
    # Basic colors
    "black": '<span style="color:black">@@</span>',
    "red": '<span style="color:red">@@</span>',
    "green": '<span style="color:green">@@</span>',
    "yellow": '<span style="color:yellow">@@</span>',
    "blue": '<span style="color:blue">@@</span>',
    "magenta": '<span style="color:magenta">@@</span>',
    "cyan": '<span style="color:cyan">@@</span>',
    "white": '<span style="color:white">@@</span>',
    # Bright colors
    "bright_black": '<span style="color:#555">@@</span>',
    "bright_red": '<span style="color:#f55">@@</span>',
    "bright_green": '<span style="color:#5f5">@@</span>',
    "bright_yellow": '<span style="color:#ff5">@@</span>',
    "bright_blue": '<span style="color:#55f">@@</span>',
    "bright_magenta": '<span style="color:#f5f">@@</span>',
    "bright_cyan": '<span style="color:#5ff">@@</span>',
    "bright_white": '<span style="color:#eee">@@</span>',
    # Background colors
    "bg_black": '<span style="background-color:black">@@</span>',
    "bg_red": '<span style="background-color:red">@@</span>',
    "bg_green": '<span style="background-color:green">@@</span>',
    "bg_yellow": '<span style="background-color:yellow">@@</span>',
    "bg_blue": '<span style="background-color:blue">@@</span>',
    "bg_magenta": '<span style="background-color:magenta">@@</span>',
    "bg_cyan": '<span style="background-color:cyan">@@</span>',
    "bg_white": '<span style="background-color:white">@@</span>',
    # Styles
    "bold": '<span style="font-weight:bold">@@</span>',
    "dim": '<span style="opacity:0.6">@@</span>',
    "italic": '<span style="font-style:italic">@@</span>',
    "underline": '<span style="text-decoration:underline">@@</span>',
    "blink": '<span style="text-decoration:blink">@@</span>',
    "reverse": '<span style="filter:invert(100%)">@@</span>',
    "hidden": '<span style="visibility:hidden">@@</span>',
    "strike": '<span style="text-decoration:line-through">@@</span>',
    "normal": "<span>@@</span>",
}

def write_stdout(text: str):
    sys.stdout.write(text)
    sys.stdout.flush()


def net_logger(text, color="white", style="normal", newline=False):
    if SETUP_COLORS == "none":
        write_stdout(text)

    palette = COLORS
    if SETUP_COLORS == "html":
        palette = COLORS_HTML

    context = str(text).split("\n")
    save_context = ""
    for item in context:
        base = palette[color].replace("@@", item)
        base = palette[style].replace("@@", base)
        write_stdout(base + "\n")

        if ENABLE_LOGGER:
            save_context = save_context + base

    if newline:
        write_stdout("\n\n")

    if ENABLE_LOGGER:
        path = f"{DATAROOT}logs/net.log"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a") as file:
            file.write(save_context)
            file.close()


def net_exec(command: str) -> dict:
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    stdout, stderr = process.communicate()
    return {
        "stdout": stdout.strip(),
        "stderr": stderr.strip(),
        "status": process.returncode,
    }


def net_checks(list_of_checks: list, enable_output: False):
    if list_of_checks.len() == 0:
        return

    for item in list_of_checks:
        check = net_exec(item)
        if enable_output:
            net_logger(check.stdout)
            net_logger(check.stderr, "red")


def read_db():
    database = None
    root = f"{DATAROOT}database/rocketdb_v2.json"
    with open(root, "r") as file:
        database = json.load(file)
        file.close()

    return database.get("index")


def eyeliner(text, color="cyan", symbol="░"):
    steps = 128
    spacer = " " * int(steps // 2 - len(text) // 2)
    data = symbol * steps + "\n" + spacer + text + "\n" + symbol * steps + "\n"
    net_logger(data, color, "bold", True)


def search_arg(args: list, keyword: str, enforce_keyword=True):
    hold_next = False
    for arg in args:
        if hold_next == True:
            return arg

        if arg == f"--{keyword}":
            hold_next = True

    if enforce_keyword == False:
        return None

    net_logger(
        f"[error] :: value for argument '{keyword}' not provided, aborting!",
        "red",
        "bold",
        True,
    )
    sys.exit(1)(128)


def dynamic_manual(args_v, man_page=False):
    database = read_db()
    bind_name = search_arg(args_v, "page", False)

    if man_page:
        with open(f"{DATAROOT}/manual/manual.txt") as file:
            net_logger(file.read(), "cyan", "bold", True)

    for bind in database:
        net_logger(f"name: {bind.get("name")}", "cyan", "bold")
        net_logger(f"description: {bind.get("description")}", "cyan", "normal")
        net_logger(f"type: {bind.get("type")}", "cyan", "normal")
        if bind.get("extends") != {}:
            net_logger(f"extends: {bind.get("extends")}", "cyan", "normal")

        arguments = bind.get("arguments")
        if arguments is not None:
            for arg in arguments:
                net_logger(
                    f"\t--{arg}\t\t{bind.get('arguments').get(arg).get('description')}",
                    "magenta",
                    "normal",
                )
                argument_options = bind.get("arguments").get(arg).get("options")
                if argument_options != None:
                    net_logger("\t\targuments:\n")
                    for opt in argument_options:
                        net_logger(f"\t\t{opt}")
        print("\n")

def net_parser(args_v: list):
    if len(args_v) == 0:
        return None

    database = read_db()
    bind_name = args_v[0]
    output = None

    for bind in database:
        if bind_name == bind.get("name"):
            cmd = bind.get("command")
            arguments = bind.get("arguments")
            if arguments is not None:
                for arg_name in arguments:
                    arg_value_from_cli = search_arg(args_v, arg_name)
                    if arg_value_from_cli:
                        cmd = cmd.replace(f"@@{arg_name}", arg_value_from_cli)

            output = net_exec(cmd)

    if output is not None:
        if output.get("stderr"):
            eyeliner(
                f"[exec] :: {bind_name} have been executed with a failure, but haven't crash!"
            )

            net_logger(output.get("stderr"))

        if output.get("stdout"):
            eyeliner(f"[exec] :: {bind_name}")
            net_logger(output.get("stdout"))

        return output.get("status")

    return 128


def raw_requests(
    url: str,
    method: str = "get",
    protocol: str = "http",
    authorization: str = "",
    body: str = "none",
    data: str = "",
    save: bool = False,
):
    """
    Execute a curl command dynamically using shell syntax.

    This function emulates a request builder, directly composing
    a curl shell command and executing it. No HTTP library is used.

    Parameters:
        url (str): Target URL. Required. Example: "http://example.com"
        method (str): HTTP method. Defaults to "get". Example: "post"
        protocol (str): Forces protocol override ("http" or "https"). Rewrites URL if needed.
        authorization (str): Authorization header content. Example: "Bearer token"
        body (str): Payload type. Accepted values:
            - "none": No body
            - "form-data": Use -F
            - "x-www-urlencoded": Use --data-urlencode
            - "raw": Use -d
            - "binary": Use --data-binary @file
        data (str): Payload content. Required if body is not "none".
        save (str): If "yes", saves output to "response.txt".

    Returns:
        dict: A netlibpy output dict

    Side-effects:
        - Prints constructed curl command.
        - Executes command using `subprocess.getoutput()`.
        - If save == "yes", writes output to "response.txt".
    """
    if protocol.lower() == "https":
        url = url.replace("http:", "https:")

    cmd = [
        "curl",
        "-A",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "-s",
        "-X",
        method.upper(),
    ]

    if authorization:
        cmd.extend(["-H", f"Authorization: {authorization}"])

    if body != "none" and data:
        if body == "form-data":
            cmd.extend(["-F", data])
        elif body == "x-www-urlencoded":
            cmd.extend(["--data-urlencode", data])
        elif body == "raw":
            cmd.extend(["-d", data])
        elif body == "binary":
            cmd.extend(["--data-binary", f"@{data}"])

    cmd.append(url)
    output = net_exec(cmd)
    net_logger("[INFO] Response received")

    if save:
        eyeliner("[function] :: requests")
        net_logger(output)

    return output

def chrome(url: str, mode: str, window_size: str = None) -> dict:
    if window_size is not None:
        window_arg = f"--window-size={window_size} "
    else:
        window_arg = "--window-size=1920,1080 "

    headless_args = (
        f"{HEADLESS_BROWSER_BIN} "
        "--enable-unsafe-swiftshader "
        "--headless=new "
        "--disable-gpu "
    )

    if mode == "dom":
        command = headless_args + "--dump-dom " + window_arg + url
    elif mode == "pdf":
        command = headless_args + "--print-to-pdf " + window_arg + url
    elif mode == "screenshot":
        command = headless_args + "--screenshot " + window_arg + url
    else:
        net_logger(f"Invalid mode: {mode}", color="red", style="bold")
        return {}

    buffer = net_exec(command)

    if buffer != {}:
        return buffer

    return {}

def get_args_v():
    return sys.argv

def net_shell_router(fn_registry = {}):
    args_v = get_args_v()
    args_v.pop(0)

    global SETUP_COLORS
    for config in args_v:
        if config == "--output_mode_html":
            args_v.remove("--output_mode_html")
            SETUP_COLORS = "html"
        
        if config == "--output_mode_none":
            args_v.remove("--output_mode_none")
            SETUP_COLORS = "none"

    if len(args_v) == 0:
        net_logger(BANNER, "magenta", "bold", True)
        exit(0)

    name = args_v[0]

    if name == "version":
        net_logger(VERSION, "green", "bold", True)
        exit(0)

    if name == "help":
        dynamic_manual(args_v)
        exit(0)

    if name == "manual":
        dynamic_manual(args_v, True)
        exit(0)

    if fn_registry != {}:
        fn_name = args_v[0]
        fn_func = fn_registry.get(fn_name)
        if fn_func is not None:
           sys.exit(fn_func(args_v))
                

    output = net_parser(args_v)
    if output == 128:
        if ENABLE_ARBITRARY_SHELL:
            output = net_exec(" ".join(args_v))
            exit(output.get("status") or 0)
