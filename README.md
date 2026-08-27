# 🖥️ PC-Control MCP Server

An MCP tool server that gives Claude Desktop control of a Windows machine — shell execution,
system stats, audio and power, screenshots, window and process management.

## How it works

The server is the **tool side** of an agent loop. It does not decide when to act; it publishes
a set of callable tools and executes them when the client asks.

```
Claude Desktop  ──MCP/stdio──▶  FastMCP server (main.py)
                                      │
                                      ├── tools/shell.py         execute_command
                                      ├── tools/system.py        get_system_status
                                      ├── tools/audio.py         manage_volume
                                      ├── tools/power.py         manage_power
                                      ├── tools/app_launcher.py  launch_application
                                      ├── tools/processes.py     get_process_list
                                      ├── tools/screen.py        take_screenshot
                                      └── tools/window.py        list_windows, manage_window
```

Each tool is registered with an `@mcp.tool()` decorator over a plain typed function:

```python
@mcp.tool()
def system_manage_volume(action: str, level: int = None) -> str:
    """
    Control system audio volume.
    Args:
        action: 'set', 'get', 'mute', 'unmute'
        level: 0-100 (required for 'set')
    """
    return manage_volume(action, level)
```

The signature and docstring **are** the tool schema — that is how the client discovers what
exists, what arguments it takes, and when to call it. Which means the docstring is an interface
contract, not a comment: a vague one produces a tool the model calls at the wrong time.

Two design choices worth naming:

- **Transport separated from behaviour.** `main.py` holds only registration; every tool body
  lives in `tools/`. So `verify_tools.py` can exercise the tools directly, without an LLM in the
  loop — when something misbehaves, that separates "the tool is broken" from "the model called
  it wrong."
- **Destructive actions are explicit.** Power management takes an `action` enum that includes
  `abort`, so a shutdown started by mistake can be cancelled.

`web-frontend-mcp/` is a second, separate server covering browser-side tooling.

⚠️ This server executes arbitrary shell commands on the host by design. Run it only against a
client you control.

### Verification

`verify_tools.py` and `verify_new_tools.py` call each tool directly and print the result. These
are smoke checks, not a test suite — no assertions, no fixtures, no CI.

## Quick Install

1. **Clone or download this folder**

2. **Install dependencies:**

```powershell
pip install -r requirements.txt
```

3. **Configure Claude Desktop:**

Edit: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "pc-control": {
      "command": "python",
      "args": ["C:/path/to/pc-control-mcp/main.py"]
    }
  }
}
```

4. **Restart Claude Desktop**

## Usage

Ask Claude:

- "Check my system status"
- "Execute command: dir"
- "Set volume to 50%"
- "Open Chrome"
- "Lock my computer"

## Requirements

- Python 3.8+
- Windows 10/11
- Claude Desktop App

## Tools

### system_execute_command

Execute any shell command

### system_get_status

Get CPU, Memory, Disk, Battery status

### system_manage_volume

Control audio volume (set, get, mute, unmute)

### system_manage_power

Power actions (shutdown, restart, sleep, lock)

### system_launch_app

Launch applications by name

### system_get_processes

List running processes sorted by CPU or Memory

### screen_take_screenshot

Capture screenshot of primary monitor

### window_list

List specific details of all visible windows

### window_manage

Manage windows (focus, minimize, maximize, close)

## License

MIT

Created with ❤️ for Windows automation
