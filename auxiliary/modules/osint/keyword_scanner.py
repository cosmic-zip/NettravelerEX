import json
import os
from urllib.parse import quote as url_encode
from auxiliary.netlibpy.netlib import *


def keyword_scanner(expression: str, verbosity="min") -> list:
    # Load osint database
    osint_db_path = os.path.join(DATAROOT, "osint", "osintdb.json")
    with open(osint_db_path, "r") as f:
        osintdb = json.load(f)

    search_result = []
    encoded_expression = url_encode(expression).replace("%", "%%")

    for item in osintdb["index"]:
        url = (
            item["url"]
            .replace("=//", "://")
            .replace("@@expression", encoded_expression)
        )

        match_positive = item.get("match_positive", [])
        match_negative = item.get("match_negative", [])

        # Fetch page content using headless chrome
        headless_dom = chrome(url, "dom")
        if not headless_dom:
            return []

        headless_dom = headless_dom.lower()

        positive = []
        negative = []

        if expression.lower() in headless_dom:
            positive.append(expression)

        for v in match_negative:
            if v.lower() in headless_dom:
                negative.append(v)

        for v in match_positive:
            if v.lower() in headless_dom:
                positive.append(v)

        result = {
            "url": url,
            "positive": positive,
            "negative": negative,
        }

        if positive and not negative:
            result["status"] = utils.colorize("FOUND", "green")
        elif positive and negative:
            result["status"] = utils.colorize("MAY_FOUND", "yellow")
        else:
            result["status"] = utils.colorize("NOT_FOUND", "red")

        search_result.append(result)

        if verbosity != "":
            net_logger("[socialnet] :: search result: ", "bright_white", "bold", True)
            net_logger(f"\turl: {result['url']}", "bright_blue", "italic")

        if verbosity in ["info", "all"]:
            net_logger(f"\tstatus: {result['status']}", "bright_blue", "italic")
            net_logger(
                f"\tpositive patterns: {len(result['positive'])}",
                "bright_blue",
                "italic",
            )
            net_logger(
                f"\tnegative patterns: {len(result['negative'])}",
                "bright_blue",
                "italic",
                True,
            )

        if verbosity == "all":
            net_logger("\textra domain info: ", "blue", "bold", True)
            net_logger(
                f"\tcategory: {item.get('category', '')}", "bright_blue", "italic"
            )
            net_logger(
                f"\tglobal rank: {item.get('global_rank', '')}", "bright_blue", "italic"
            )
            net_logger(f"\tcountry: {item.get('country', '')}", "bright_blue", "italic")
            net_logger(f"\tnsfw: {item.get('nsfw', '')}", "bright_blue", "italic", True)

    return search_result


def keyword_scanner_wrapper(args_v):
    expression = search_arg(args_v, "expression")
    verbosity = search_arg(args_v, "verbosity")

    if keyword_scanner(expression, verbosity) is not None:
        return 0

    return 255
