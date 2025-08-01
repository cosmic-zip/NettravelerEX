base_html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <link rel="stylesheet" href="assets/ui.css">
        <script src="assets/ui.js"></script>
        <title>@@PAGETITLE</title>
        <script>function toggleSection(sectionId) { const sections = document.querySelectorAll('section'); sections.forEach(section => { if (section.id === sectionId) { section.style.display = 'block' } else { section.style.display = 'none' } }) }</script>
        <script>function downloadDivAsTxt(divId, filename) { const div = document.getElementById(divId); if (!div) { console.error('Div not found:', divId); return } const text = div.textContent || ''; const blob = new Blob([text], { type: 'text/plain' }); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = filename || 'download.txt'; document.body.appendChild(a); a.click(); document.body.removeChild(a); URL.revokeObjectURL(url) }</script>
    </head>

    <body>
        <header><span><em>いらっしゃい</em></span></header>
        <main>
            <div class="sidebar">
                <div>@@SIDEBAR</div>
            </div>
            <div class="container"><input type="hidden" id="ztoken" name="ztoken" value="@@ZTOKEN">
                <section class="content-sec" id="default"></section>
                @@EXTENDS
                @@CONTAINER
            </div>
        </main>
    </body>

    </html>
"""

# SIDEBAR
sidebar_groups = """
    <h3>Home</h3>
    <button type="submit" class="sidebar-submit" onclick="toggleSection('default')">Home</button>
    <h3>extensions</h3>
        @@EXTENSIONS
    <h3>system</h3>
        @@SYSTEM
"""


sidebar_button = """<button type="submit" class="sidebar-submit" onclick="toggleSection('@@IDSECTION')">@@BTNAME</button>"""


# SECTION_CONTENT
section = """
    <section class="content-sec" id="@@IDSECTION">
        <header class="sec-header">
            <span><em>@@TITLE</em></span>
        </header>
        <div class="outputer">
            <pre id="@@IDOUTPUT">
            </pre>
        </div>
        <div class="hint" id="hint_session">
            <button onclick="downloadDivAsTxt('@@IDOUTPUT', 'output.txt')" class="btn-downloader">Download</button>
            @@HINT 
        </div>
        <div class="hint hint-error" id="error_session">
            @@ERROR
        </div>
        <form class="form-ctn" method="post"> 
            @@FORM_CONTENT 
            <div class="form-text">
                <h3 class="form-title">HACK NOW!</h3>
                <input type="hidden" id="requestid@@REQUESTID" name="requestid@@REQUESTID" value="@@REQUESTID">
                <input type="hidden" id="EZEC@@MNAME@@REQUESTID" name="EZEC@@MNAME@@REQUESTID" value="@@MNAME">
                <input type="submit" class="form-text-submit"
                    hx-post="@@GEN_HOST"
                    hx-include="@@IDFNAME_LIST #requestid@@REQUESTID, #EZEC@@MNAME@@REQUESTID, #ztoken"
                    hx-target="@@IDOUTPUTHTX"
                    hx-trigger="click">
            </div>
        </form>
        
    </section>
"""


section_header = """
    
"""
section_outputer = """
    <div class="outputer">
        <pre id="IDOUTPUT">
        </pre>
    </div>
"""


section_outputer_xl = """
    <div class="outputer outputer-xl"></div>
"""

section_hint = """
    <div class="hint" id="hint_session">
        <button onclick="downloadDivAsTxt('IDOUTPUT', 'output.txt')" class="btn-downloader">Download</button>
        @@HINT 
    </div>
"""

section_error = """
    <div class="hint hint-error" id="error_session">
        @@ERROR
    </div>
"""

section_form = """
<form class="form-ctn" method="get"> @@FORM_CONTENT </form>
"""

section_form_text = """
    <div class="form-text">
        <h3 class="form-title">@@FTITLE</h3>
        <input type="text" class="form-text-input" name="@@IDFTITLE" id="@@IDFTITLE">
    </div>
"""
section_form_select = """
    <div class="form-text">
        <h3 class="form-title">@@FTITLE</h3>
        <select name="@@IDFNAME" id="@@IDFNAME" class="form-select">
            @@FOPTIONS
        </select>
    </div>
"""

section_form_select_options = (
    """<option value="@@FOPTION_VALUE">@@FOPTION_NAME</option>"""
)


section_form_submit = """
    <div class="form-text">
        <h3 class="form-title">HACK NOW!</h3>
        <input type="hidden" id="requestid@@REQUESTID" name="requestid@@REQUESTID" value="@@REQUESTID">
        <input type="hidden" id="EZEC@@MNAME@@REQUESTID" name="EZEC@@MNAME@@REQUESTID" value="@@MNAME">
        <input type="submit" class="form-text-submit"
            hx-post="@@GEN_HOST"
            hx-include="@@IDFNAME_LIST #requestid@@REQUESTID, #EZEC@@MNAME@@REQUESTID, #ztoken"
            hx-target="@@IDOUTPUT">
    </div>
"""
