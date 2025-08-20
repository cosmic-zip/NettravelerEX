!['banner'](spellbook/webui/assets/banner.png)

![banner](spellbook/webui/assets/lineBar.png)

![NettravelerEX](https://img.shields.io/github/actions/workflow/status/cosmic-zip/NettravelerEX/netex.yml)
![GitHub issues](https://img.shields.io/github/issues/cosmic-zip/NettravelerEX)
![GitHub top language](https://img.shields.io/github/languages/top/cosmic-zip/NettravelerEX)
 [![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

## NettravelerEX

NettravelerEX is an offensive security toolkit that aggregates tools, serializes functions, and provides a standardized interaction interface for various tasks including Wi-Fi hacking, web scanning, vulnerability scanning, OSINT, forensics, backup management, SQL injection, backdoor and ransomware management, custom malware building, reverse shells, RCE agents, generation of reports (RBR), and playbooks (RBP) based on rules.

It also has a WebUI that provides access to all CLI features and includes custom extensions. The WebUI is automatically generated, so all modifications made by the user will be available after executing the `build.web` sub-command.

The system works through a "genesis" file, which registers all commands, aliases, binds, and functions, along with their documentation and super-strings. Each super-string contains information about predefined options for external software or internal functions. With this design, and the fact that documentation and manuals are automatically generated, we have a complete, extensible, and robust system ready for operational use.

NettravelerEX features an automated playbook generation system based on vulnerability and attack databases from OWASP and AI support. It supports English and Brazilian Portuguese versions. This system is also used to generate bug bounty reports.

From the genesis file, a parser combined with a template engine (built from scratch) generates Web, CLI, and API interfaces. The most commonly used are CLI and Web. The API interface is experimental and may not function correctly.

**Important: This project has a custom web server implemented from scratch using GO. This server allows code execution and remote command execution, so it must not be exposed to any network. Always run it in localhost or inside a NATed virtual machine.**

The user (you) interacts only with the interfaces, which provide a standardized way to engage with all submodules, extensions, plugins, and native functions.

NettravelerEX does not rely on third-party libraries. It uses only code developed directly in Python, making it highly portable, durable, and easy to install. Wherever a GNU/coreutils or coreutils-compatible system exists, NettravelerEX will run.

## Installation:

todo 

env variables: 

* NT_DATAROOT → Set the spellbook location

## How to use:

```console
nettraveler [submodule] --arg1 value --arg2 option --arg3 123
```

Whenever executing any function in NettravelerEX, you always start by defining which submodule to use, followed by arguments written with `--`. The argument names are not standardized anymore, but they meaning can be found in the rocketdb.json

About the submodule cosmic: Cosmic is my nickname, and I used it to address small and self-contained submodules that would otherwise create unnecessary overhead.

Example:

```console
chmod +x nettraveler.py
./nettraveler.py version
```

## Output modes

### color (default)

Adds **ANSI terminal colors** using UNIX escape codes. Suitable for **interactive terminals**. Not safe for log files or automation.

Example:

```bash
./nettraveler version
```

### none

Outputs **plain UTF-8 text**, no colors or formatting. Ideal for **scripts**, **logs**, and **automation**.

Example:

```bash
./nettraveler version --output_mode_none
```

### html

Generates **HTML-formatted output** using inline `<span>` and `style`. Used for **dashboards**, **reports**, and **web previews**.

Example:

```bash
./nettraveler version --output_mode_html
```

## Read the Manual!

```console
./nettraveler manual
```

# FLAGS SCLF

Standard Command-Line Flags (SCLF) include:

- `account` : Arguments for account info or token.
- `address` : IPv4/IPv6 or domain name.
- `ip` : IPv4/IPv6 address.
- `device` : Virtual/physical device (e.g., HDD, SSD).
- `dns/domain` : Domain name.
- `database_name` : Name of the database.
- `data` : Input data (e.g., "some data here!").
- `file` : File location.
- `folder` : Path to a folder.
- `host` : Hostname or IP address.
- `image` : Image file location.
- `interface` : Network device.
- `keyspace_name` : Cassandra keyspace name.
- `message` : Message string.
- `output` : Output file path.
- `overwrite` : Overwrite existing files.
- `password` : Plaintext password.
- `path` : File path.
- `port` : Port number.
- `protocol` : Communication protocol.
- `recursive` : Enable recursive mode.
- `secret` : File (data) to be hidden.
- `share` : Shared resource (e.g., folder, file, printer).
- `snapshot_name` : Name of the snapshot.
- `table_name` : Database table name.
- `target` : IPv4/IPv6 or domain name.
- `timeout` : Timeout duration.
- `url` : Full URL path with http/https.
- `username` : Username setup.
- `wait` : Delay duration in seconds.
- `verbose` : Enable verbose mode.
- `wordlist` : Path to a wordlist.


## How to create plugins

There are three ways to create plugins in NettravelerEX: by using the rocketdb.json, by creating a new domain inside auxiliary/modules, or by modifying the WebUI. In general: external shell commands go to rocketdb as a super-string, python code is separated between logic and implementation. Logic goes to auxiliary/modules/mod_name and the real implementation goes to infra/, such as network functions, headless browsers, or other low-level functions. In the end, everything must be registered in rocketdb, except for extensions, templates, and WebUI components.

Each file of your app can export more than one function, but you must return only the final functions. All must accept argsv as a parameter, even if it is not used. In the example above, `sample_scan` does not use argsv, but it still requires the `_` (underscore) as a parameter.

-- auxiliary/settings.lua

```python
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
```

-- data/database/rocketdb.json

```json
{
  "index": [
    {
      "arguments": {
        "value": {
          "description": "Dummy example"
        }
      },
      "command": "echo @@value",
      "description": "Random summy bind for testing",
      "extends": {},
      "name": "test.dummy",
      "type": "shell"
    }
  ]
}
```

As you can see, the term `native.` indicates to the parser that it is a function, not an external software call. Arguments such as `address` and `option` are marked with `@@`, meaning they are magic_docs arguments.

To define predefined options:

-- data/database/rocketdb.json

```json
{
  "index": [
            {
            "arguments": {
                "scripts": {
                    "description": "Setup one of nmap default scripts",
                    "options": [
                        "auth",
                        "broadcast",
                         ...
  						  ...
                        "traveler"
                    ]
                },
                "target": {
                    "description": "Refers to an IPv4 or IPv6 or domain name"
                }
            },
            "command": "scan.nmapper @@target @@scripts",
            "description": "Perform NMAP scanning",
            "name": "native.scanner.nmapper"
        },
  ]
}
```

Now, `@@option` tells the parser that `foo` and `bar` are valid predefined options for the `option` argument. Execution would look like this:

```console
nettraveler scanner.myapp --address 172.16.123.123 --option foo
```

## How external aliases and binds work

The first example shows a simple alias that does not require any arguments. The second example requires an argument named address.

```json
{
  "index": [
    {
      "command": "ss -tupran",
      "description": "Scan local open connections",
      "extends": {},
      "name": "map.local",
      "type": "shell"
    },
    {
      "command": "curl ip.me",
      "description": "Show the current ip address",
      "extends": {},
      "name": "map.myip",
      "type": "shell"
    }
  ]
}
```

Execution examples:

```console
nettraveler map.local
nettraveler ftp.connect --address 172.16.123.123
```

## WebUI

The **WebUI** is a simple **SPA** (Single Page Application) built from scratch using **HTMX**. The preference for **HTMX** instead of **React** or any other library is due to its simplicity, and the fact that you don't need to install anything besides **coreutils** and some CLI tools like **nmap**. In the near future, you may find a folder inside `data` called `mod/webui`; any file placed in this folder will be included inside the final **SPA**.

While creating this framework, sometimes there was a need to fill a form, but directly in the terminal it felt limiting. So the idea came: why not just use an **HTML** form and an **API**? From that thought, and after three attempts, this **WebUI** was created. It's portable, simple, extensible, and more: it is generated using `nettraveler build.web`, making it easy to maintain and upgrade through the **extensions system**.

The WebUI must run on the same IP address and port as the server. For example, if the WebUI is configured for 127.0.0.1:5500, the server must also use this address—otherwise, requests will fail. Additionally, the WebUI and server must share the same token. This token is not for authentication but acts as an owner identifier. Be aware that all communication happens in plain text, so use this setup only in secure environments.

## Templates

### What is a Template?

A **template** is a **python variable** containing **HTML** code and `@@UPPERCASE` placeholders. At the end of the module, you should export (return) only the table. Templates should be **simple**, **small**, and **reusable**. If your code is unique and not general-purpose, you may prefer to build one or more **extensions** instead.

Example:

```python
section_form_select = """
    <div class="form-text">
        <h3 class="form-title">@@FTITLE</h3>
        <select name="@@IDFNAME" id="@@IDFNAME" class="form-select">
            @@FOPTIONS
        </select>
    </div>
"""
```
## Extensions

### What is a Extension?

**extensions** are a special kind of **component**, but with a very specific structure. These extensions contain a fixed base structure and must follow a pattern like the example below. In short, you will have a `<section>` tag like `<section class="content-sec" id="SOMENAME">` and a corresponding button like `<button type="submit" class="sidebar-submit" onclick="toggleSection('SOMENAME')">SOMENAME</button>`. As you can see, `SOMENAME` has a clear role to identify the section and link it to the **SPA** logic. This name should always be **unique** and **lowercase**.

```python
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
    "button": '<button type="submit" class="sidebar-submit" onclick="toggleSection(\'haki\')">㊊ Haki search</button>'
}
```

## Embedded Server

This server addresses multiple concerns: it is **portable**, **statically linked**, and **free of external dependencies**, consistent with the overall design of the project. It also enables a **web interface to be served easily**, even in **restricted environments** such as **Orange Pi** or **smartphones**.

To serve the WebUI using the server, run:

```console
nettraveler server --host 127.0.0.1 --port 5500 --folder webui/
```

The server will create a log file named `evil_server.log` containing all **POST requests**. If the IP address you provide matches the value set in the `GEN_HOST` global variable within the WebUI, the server will operate as intended and serve the page normally. However, if a different IP or port is configured, the page will still be served, but **command requests will be blocked by default**.

To serve a static or malicious page manually, use the following command:

```console
nettraveler server --host 127.0.0.1 --port 5500 --folder data/evilpages/default
```

Let me know if you want the GEN_HOST behavior hardened or fallback logic implemented.

## Artificial Inteligency Assistant

It's the default LLaMA with some tweaks and using an uncensored AI model. To serve the WebUI with the AI assistant, you need at least 12 GB of RAM and must run the full web server with `--full yes`.

```console
nettraveler server.yuri --host 127.0.0.1 --port 5500 --folder webui/ --full yes
```

**or by using the default option**

```console
nettraveler server.default
```

## Playbooks and Reports

The `cosmic.report` module is a **comprehensive feature** for generating manual and autonomous security reports. It was originally designed for **bug bounty operations**, but it is **not limited to vulnerability disclosure**—it can support any structured Red Team or assessment reporting. All generated reports are saved to the path: `DATAROOT/reports` (typically `data/reports/`).

This module includes two main stages:

1. A **selection stage**, where it generates a list of vulnerabilities and attacks for a specified language (such as **English** `en` or **Portuguese** `br`). These are mapped using OWASP-based lists.
2. A **configuration stage**, where you define a set of parameters to customize how the report is generated.

The following table explains each parameter available for report generation:

| Parameter         | Optional | Description                                                                        |
| ----------------- | -------- | ---------------------------------------------------------------------------------- |
| `title`           | No       | Sets the report title. This also determines the output file name.                  |
| `lang`            | No       | Sets the report language. Currently supports `en` (English) and `br` (Portuguese). |
| `vulns_options`   | Yes      | Lists all mapped OWASP-based vulnerabilities available for selection.              |
| `attacks_options` | Yes      | Lists all mapped OWASP-based attack types available for selection.                 |

| Parameter     | Optional | Description                                                                      |
| ------------- | -------- | -------------------------------------------------------------------------------- |
| `noprint`     | Yes      | If set to `yes`, the report is not written to disk.                              |
| `system_type` | Yes      | Defines the target stack or platform, e.g., `web/html`, `web/api`, `mobile/apk`. |
| `vector`      | Yes      | Specifies the domain, URL, or application name being tested.                     |
| `stack`       | Yes      | Describes the technologies in use: `html`, `css`, `js`, `java`, `asp`, etc.      |
| `vulns`       | Yes      | List of vulnerability IDs to include, e.g., `1`, `1,2`, or `1,44,22`.            |
| `attacks`     | Yes      | List of attack IDs to include, following the same format as `vulns`.             |
wdwdwdnada?
**Risk Rating System**

| Level (0-10)       | Severity                                                                            |
| ------------------ | ----------------------------------------------------------------------------------- |
| **10 - Critical**  | Exploitation can cause severe damage (e.g., data breaches, full system compromise). |
| **7-9 - High**     | Significant vulnerability but may require specific conditions to exploit.           |
| **4-6 - Medium**   | Moderate impact, often exploitable in combination with other flaws.                 |
| **1-3 - Low**      | Minimal risk, usually related to suboptimal configurations.                         |
| **0 - Negligible** | No direct security impact, but improvements are possible.                           |

## Cosmic Guide for Hacking

### Checkout [cosmic wiki](https://cosmic-zip.github.io/)

## LICENSE

This project is licensed under the GNU General Public License v3.0. NettravelerEX includes IP2Proxy® LITE and cinsscore® databases.