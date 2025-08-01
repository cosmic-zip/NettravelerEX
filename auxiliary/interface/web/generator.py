from auxiliary.interface.web.templates.base import *
from auxiliary.netlibpy.netlib import *
from auxiliary.interface.web.extensions.ext_registry import mods
import random


def gen_base(args_v=None):
    base = base_html
    base = base.replace("@@PAGETITLE", GEN_TITLE)
    database = read_db()

    overall_sections = []
    overall_buttons = []
    for item in database:

        seed = str(random.randint(101010, 991199))

        buttom = sidebar_button.replace("@@IDSECTION", seed)
        buttom = buttom.replace("@@BTNAME", item.get("name"))
        overall_buttons.append(buttom)
        new_sec = section.replace("@@IDSECTION", seed)
        new_sec = new_sec.replace("@@IDOUTPUTHTX", "#ID" + seed)
        new_sec = new_sec.replace("@@IDOUTPUT", "ID" + seed)
        new_sec = new_sec.replace("@@REQUESTID", seed)
        new_sec = new_sec.replace("@@TITLE", item.get("name"))
        new_sec = new_sec.replace("@@HINT", item.get("description"))
        new_sec = new_sec.replace("@@MNAMEZ", item.get("name"))
        new_sec = new_sec.replace("@@MNAME", item.get("name"))

        # idk
        type = item.get("type")
        extends = item.get("extends")

        arguments = item.get("arguments")
        args_buffer = []
        id_list = []
        if arguments:
            args = item["arguments"]
            for arg in args:

                arg_obj = args.get(arg)
                if arg_obj.get("options"):
                    arg_options = arg_obj.get("options")

                    buffer = []
                    for opt in arg_options:
                        buffer.append(
                            section_form_select_options.replace("@@FOPTION_NAME", opt)
                        )

                    new_select = section_form_select.replace("@@IDFNAME", arg)
                    id_list.append(arg)
                    new_select = section_form_select.replace(
                        "@@FOPTIONS", "\n".join(buffer)
                    )
                    args_buffer.append(new_select)

                else:
                    new_text = section_form_text.replace("@@FTITLE", arg)
                    id_list.append(arg)
                    new_text = new_text.replace("@@IDFTITLE", arg)
                    args_buffer.append(new_text)

        ids = ""
        for x in id_list:
            ids = ids + "#" + x + ", "
        new_sec = new_sec.replace("@@IDFNAME_LIST", ids)
        new_sec = new_sec.replace("@@FORM_CONTENT", "\n".join(args_buffer))
        new_sec = new_sec.replace("@@GEN_HOST", GEN_HOST)
        overall_sections.append(new_sec)

    sbar = sidebar_groups.replace("@@SYSTEM", "\n".join(overall_buttons))
    base = base.replace("@@ZTOKEN", COSMIC_SIGKEY)
    base = base.replace("@@SIDEBAR", sbar)
    base = base.replace("@@CONTAINER", "\n".join(overall_sections))
    return base


def gen_extends():
    base = gen_base()
    # ADD extensions
    ext = mods()

    buttoms = "\n".join(ext.get("buttoms"))
    sections = "\n".join(ext.get("sections"))

    base = base.replace("@@EXTENSIONS", buttoms)
    base = base.replace("@@EXTENDS", sections)
    base = base.replace("@@ERROR", "neko hackers inside >_<")
    return base


def gen_wrapper(args_v=None):
    print(gen_extends())
    return 0
