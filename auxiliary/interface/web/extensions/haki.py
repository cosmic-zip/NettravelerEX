haki ="""
<section class="content-sec" id="haki">
        <div class="haki">
            <div class="haki-search-ctn">
                <input type="text" class="haki_search" id="haki_search" name="haki_search"
                    placeholder="Enter NettravalerEX.v6 script here!">
                <input class="haki_search haki_go" type="submit" hx-get="@@GEN_HOST"
                    hx-include="#haki_search" hx-target="#haki_output">
            </div>
            <div class="outputer haki_putter" id="haki_output">
                <p>neko hackers inside >_<</p>
            </div>
        </div>
    </section>
"""

haki = {
    "section": haki,
    "buttom": '<button type="submit" class="sidebar-submit" onclick="toggleSection(\'haki\')">㊊ Haki search</button>'
}