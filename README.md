# 🖥️ PC-Control MCP Server

Simple and lightweight MCP server for controlling Windows PC via Claude Desktop.

## Features

✅ **Execute Shell Commands** - Run any Windows command
✅ **System Status** - Check CPU, Memory, Disk usage
✅ **Audio Control** - Manage system volume
✅ **Power Management** - Shutdown, restart, sleep, lock
✅ **App Launcher** - Launch any application
✅ **Vision** - Take screenshots
✅ **Window Control** - Minimize, maximize, focus windows
✅ **Process Manager** - Monitor resource usage

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
