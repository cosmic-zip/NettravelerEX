from auxiliary.interface.web.extensions.docs import mod_docs
from auxiliary.interface.web.extensions.haki import haki
from auxiliary.interface.web.extensions.llama_ui import llama_ui
from auxiliary.interface.web.extensions.settings import settings


mods_reg = [
    mod_docs,
    haki,
    llama_ui,
    settings,
]

def mods():
    buttoms = []
    sections = []
    for mod in mods_reg:
        buttoms.append(mod.get("buttom"))
        sections.append(mod.get("section"))
    
    return {
        "buttoms": buttoms,
        "sections": sections
    }