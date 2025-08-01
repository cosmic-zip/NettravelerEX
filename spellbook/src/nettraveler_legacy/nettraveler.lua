#!/usr/bin/env lua
-- -------------------------------------------------
--                   NettravelerEX
-- -------------------------------------------------
local hasModule, lld = pcall(require, "lldebugger")
if hasModule then
    lld.start()
end


VERSION = "NetTraveler BETA2025.666 by COSMIC ZIP 11-APR-2025"
DATAROOT = "data/"
ENABLE_COLORS = "color" -- none color html
ENABLE_LOGGER = false
SESSION = "default"
COSMIC_SIGKEY = "b7a5f1f46944d5cc438646c547e20b177257608b5dfff41d7c5f063a6ea092fe"
GEN_HOST = 'http://127.0.0.1:5500'
GEN_TITLE = '⛩️ NettravalerEX'
HEADLESS_BROWSER_BIN = "chromium"

BANNER = [[
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                NetTraveler BETA2025.222 by COSMIC ZIP 11-APR-2025
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
NATIVE                           Exec a nettraveler native function
SCHEDULER                        Exec a binary in a scheduler with periodic or delay setup 
ARBITRARY                        Run a arbitrary command if a bind, native function or scheduler arn't found
 
MODES
 
SHELL                            Run like a shell command
INTERACTIVE                      Run with a friendly assistent (BETA)
 
HELP                             Run cosmic.manual
 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
]]


COLORS = {
    -- Basic colors
    black = "\27[30m@@\27[0m",
    red = "\27[31m@@\27[0m",
    green = "\27[32m@@\27[0m",
    yellow = "\27[33m@@\27[0m",
    blue = "\27[34m@@\27[0m",
    magenta = "\27[35m@@\27[0m",
    cyan = "\27[36m@@\27[0m",
    white = "\27[37m@@\27[0m",

    -- Bright colors
    bright_black = "\27[90m@@\27[0m",
    bright_red = "\27[91m@@\27[0m",
    bright_green = "\27[92m@@\27[0m",
    bright_yellow = "\27[93m@@\27[0m",
    bright_blue = "\27[94m@@\27[0m",
    bright_magenta = "\27[95m@@\27[0m",
    bright_cyan = "\27[96m@@\27[0m",
    bright_white = "\27[97m@@\27[0m",

    -- Background colors
    bg_black = "\27[40m@@\27[0m",
    bg_red = "\27[41m@@\27[0m",
    bg_green = "\27[42m@@\27[0m",
    bg_yellow = "\27[43m@@\27[0m",
    bg_blue = "\27[44m@@\27[0m",
    bg_magenta = "\27[45m@@\27[0m",
    bg_cyan = "\27[46m@@\27[0m",
    bg_white = "\27[47m@@\27[0m",

    -- Styles
    bold = "\27[1m@@\27[0m",
    dim = "\27[2m@@\27[0m",
    italic = "\27[3m@@\27[0m",
    underline = "\27[4m@@\27[0m",
    blink = "\27[5m@@\27[0m",
    reverse = "\27[7m@@\27[0m",
    hidden = "\27[8m@@\27[0m",
    strike = "\27[9m@@\27[0m",
    normal = "@@",
}

COLORS_HTML = {
    -- Basic colors
    black = '<span style="color:black">@@</span>',
    red = '<span style="color:red">@@</span>',
    green = '<span style="color:green">@@</span>',
    yellow = '<span style="color:yellow">@@</span>',
    blue = '<span style="color:blue">@@</span>',
    magenta = '<span style="color:magenta">@@</span>',
    cyan = '<span style="color:cyan">@@</span>',
    white = '<span style="color:white">@@</span>',

    -- Bright colors
    bright_black = '<span style="color:#555">@@</span>',
    bright_red = '<span style="color:#f55">@@</span>',
    bright_green = '<span style="color:#5f5">@@</span>',
    bright_yellow = '<span style="color:#ff5">@@</span>',
    bright_blue = '<span style="color:#55f">@@</span>',
    bright_magenta = '<span style="color:#f5f">@@</span>',
    bright_cyan = '<span style="color:#5ff">@@</span>',
    bright_white = '<span style="color:#eee">@@</span>',

    -- Background colors
    bg_black = '<span style="background-color:black">@@</span>',
    bg_red = '<span style="background-color:red">@@</span>',
    bg_green = '<span style="background-color:green">@@</span>',
    bg_yellow = '<span style="background-color:yellow">@@</span>',
    bg_blue = '<span style="background-color:blue">@@</span>',
    bg_magenta = '<span style="background-color:magenta">@@</span>',
    bg_cyan = '<span style="background-color:cyan">@@</span>',
    bg_white = '<span style="background-color:white">@@</span>',

    -- Styles
    bold = '<span style="font-weight:bold">@@</span>',
    dim = '<span style="opacity:0.6">@@</span>',
    italic = '<span style="font-style:italic">@@</span>',
    underline = '<span style="text-decoration:underline">@@</span>',
    blink = '<span style="text-decoration:blink">@@</span>',
    reverse = '<span style="filter:invert(100%)">@@</span>',
    hidden = '<span style="visibility:hidden">@@</span>',
    strike = '<span style="text-decoration:line-through">@@</span>',
    normal = '<span>@@</span>',
}

local function version(_)
    local buffer = colorize(VERSION, "bold")
    buffer = colorize(buffer, "cyan")
    written(buffer)
end

local function split(str, sep)
    if str == nil then return {} end
    local result = {}

    for part in str:gmatch("([^" .. sep .. "]+)") do
        table.insert(result, part)
    end

    return result
end


local function colorize(text, color)
    if ENABLE_COLORS == 'none' then
        return text
    end

    local palette = COLORS

    if ENABLE_COLORS == 'html' then
        palette = COLORS_HTML
    end

    if text == nil or color == nil then
        raise(
            "[colorize] (Kinda gay function UwU) :: Text argument can't by empty!")
    end

    local buffer = {}
    for tx in text:gmatch("[^\r\n]+") do
        tx = tx:gsub("%%", "%%%%")
        local col = palette[color]:gsub("@@", tx)
        -- if ENABLE_COLORS == 'html' then
        --     col = col
        -- end
        table.insert(buffer, col)
    end
    return table.concat(buffer, "\n")
end



local function written(text, color, style, newline)
    local stdout = io.stdout
    local buffer = {}
    if text == nil then return raise("[written] :: Text arg can't by empty!", 128) end

    local function simple_logger(written_formated)
        local path = DATAROOT .. ".cache/logger_session_" .. SESSION .. ".raw"
        local file = io.open(path, "a+")
        if file == nil then return 128 end
        file:write(written_formated)
    end

    for tx in text:gmatch("[^\r\n]+") do
        local newtx = tx
        if style ~= nil then
            newtx = colorize(newtx, style)
        else
            newtx = colorize(newtx, "normal")
        end

        if color ~= nil then
            newtx = colorize(newtx, color) .. "\n"
        else
            newtx = colorize(newtx, "white") .. "\n"
        end
        table.insert(buffer, newtx)
        stdout:write(newtx)
        simple_logger(newtx)
        io.flush()
    end


    if newline == "yes" then
        stdout:write("\n")
    end
    io.flush()
    return buffer
end

local function banner(argsv)
    if #argsv < 1 then
        written(BANNER, "magenta")
    end
end

local function exec(cmd, filter)
    local cmd_output = io.popen(cmd)

    if not cmd_output then
        utils.raise("[exec] :: Couldn't create pipe >_<")
        return ""
    end

    local result = cmd_output:read("*a")

    if result then
        local output = ""
        for line in result:gmatch("[^\r\n]+") do
            if filter then
                for _, rule in pairs(filter) do
                    if line ~= filter then
                        output = output .. line .. "\n"
                    end
                end
            else
                output = output .. line .. "\n"
            end
        end
        cmd_output:close()
        return output
    end
end


local function json_decode(file)
    local json = io.open(file, "r")
    if json == nil then return {} end

    json = json:read("*all")
        :gsub(":", "=")
        :gsub("%]", "}")
        :gsub("%[", "{")
        :gsub('"([^"]+)"%s*=%s+', '%1 =')

    json = "return " .. json
    local temp = io.open(DATAROOT .. ".cache/.temp", "w")
    if temp == nil then return {} end

    temp:write(json)
    temp:close()

    return dofile(DATAROOT .. ".cache/.temp")
end



local function json_decode(file)
    local json = io.open(file, "r")
    if json == nil then return {} end

    json = json:read("*all")
        :gsub(":", "=")
        :gsub("%]", "}")
        :gsub("%[", "{")
        :gsub('"([^"]+)"%s*=%s+', '%1 =')

    json = "return " .. json
    local temp = io.open(DATAROOT .. ".cache/.temp", "w")
    if temp == nil then return {} end

    temp:write(json)
    temp:close()

    return dofile(DATAROOT .. ".cache/.temp")
end

local function search_bind(bind_name)
    local buffer = {}

    if bind_name ~= nil then
        if string.match(bind_name, "native.") then
            return buffer
        end
    end

    local bindsdb = json_decode(DATAROOT .. "binds/rocketdb_v2.json")
    for i, entry in ipairs(bindsdb.index) do
        if entry.name == bind_name then buffer = entry end
    end
    return buffer
end


local function search_argsv(argsv, key, is_arg_optional)
    local hold_next = false
    for _, ag_val in pairs(argsv) do
        if hold_next == true then
            if ag_val == "lua" then
                written("[search_argsv] :: ag_value cannot be equal to 'lua' as the value for the field: " ..
                    key .. " not found",
                    "red", "bold", "yes")
            end
            return ag_val
        end

        if ag_val == ("--" .. key) then
            hold_next = true
        end
    end

    if is_arg_optional == "is_optional" then
        return ""
    end

    written("[error] :: value for argument '" .. key .. "' not provided, aborting!")
    sys.exit(1)(1)

end

local function shell_binds_parser(argsv, command_string)
    local command = split(command_string, " ")

    for _, value in pairs(command) do
        local raw_cmd_key = value:gsub("@@", "--")
        local hold_next = false

        for _, argsv_val in pairs(argsv) do
            if hold_next == true then
                command_string = command_string:gsub(value, argsv_val)
                hold_next = false
            end

            if argsv_val == raw_cmd_key then hold_next = true end
        end
    end

    return command_string
end

local function deliner(text, color, char)
    local char = char
    if char == nil then
        char = "░"
    end

    local string = string.rep(char, 128) ..
    "\n" .. string.rep(" ", (64 - (string.len(text) // 2))) .. text .. "\n" .. string.rep(char, 128)
    written(string, color, "bold", "yes")
end

local function arbitrary_shell(argsv)
    local buffer = exec(table.concat(argsv, " "))
    deliner(
        "[shell] :: Executing arbitrary shell command, good luck! >_<", "cyan")
    written(buffer)
    if buffer ~= nil then return 0 end
    return 128
end

local function command_registry(argsv)
    local func_name = argsv[1]
    local command_list = APPS

    for _, v in pairs(command_list) do
        if v.name == func_name then
            deliner("[native] :: " .. func_name, "cyan")
            return v.func(argsv)
        end
    end

    return 999
end

local function init_cache()
    exec("mkdir " .. DATAROOT .. ".cache 2> /dev/null")
    exec("mkdir" .. DATAROOT .. "reports 2> /dev/null")
    exec("echo '' > " .. DATAROOT .. ".cache/.temp ")
end

local function is_argsv_valid(argsv)
    if argsv ~= nil then return argsv end
    if arg ~= nil then return arg end
    written("[entry] Impossible to read command line args variable in lua")
    return {}
end

local function entry(argsv)
    argsv = is_argsv_valid(argsv)
    banner(argsv)
    init_cache()

    local color_mode = search_argsv(argsv, "outputmode", "is_optional")
    if color_mode ~= nil then
        ENABLE_COLORS = color_mode
    end

    local bind_config = search_bind(argsv[1])
    local buffer = shell_binds_parser(argsv, bind_config.command)


    if buffer ~= nil then
        deliner("[bind] :: " .. bind_config.name, "cyan")
        buffer = exec(buffer)
        if buffer == nil then return 128 end
        written(buffer)
        return 0
    end

    local result = command_registry(argsv)
    if result == 999 then
        if #argsv > 0 then
            return arbitrary_shell(argsv)
        end
    end

    return result
end


-- ENTRY POINT xD
entry()

