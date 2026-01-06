from mcp.server.fastmcp import FastMCP
import asyncio
import argparse

# Import tools
from tools.shell import execute_command
from tools.system import get_system_status
from tools.audio import manage_volume
from tools.power import manage_power
from tools.app_launcher import launch_application
from tools.processes import get_process_list
from tools.screen import take_screenshot
from tools.window import list_windows, manage_window

# Initialize the MCP server
mcp = FastMCP("PC-Control")

@mcp.tool()
def system_execute_command(command: str, cwd: str = None) -> str:
    """Execute a shell command on the host machine."""
    return execute_command(command, cwd)

@mcp.tool()
def system_get_status() -> str:
    """Get current system status including CPU, Memory, and Disk usage."""
    return get_system_status()

@mcp.tool()
def system_manage_volume(action: str, level: int = None) -> str:
    """
    Control system audio volume.
    Args:
        action: 'set', 'get', 'mute', 'unmute'
        level: 0-100 (required for 'set')
    """
    return manage_volume(action, level)

@mcp.tool()
def system_manage_power(action: str) -> str:
    """
    Perform power management actions.
    Args:
        action: 'shutdown', 'restart', 'sleep', 'lock', 'abort'
    """
    return manage_power(action)

@mcp.tool()
def system_launch_app(app_name_or_path: str) -> str:
    """Launch an application by name or path."""
    return launch_application(app_name_or_path)

@mcp.tool()
def system_get_processes(sort_by: str = "cpu", limit: int = 10) -> str:
    """
    Get a list of running processes.
    Args:
        sort_by: 'cpu' or 'memory' (default: 'cpu')
        limit: Number of processes to return (default: 10)
    """
    return get_process_list(sort_by, limit)

@mcp.tool()
def screen_take_screenshot() -> str:
    """
    Take a screenshot of the primary monitor.
    Returns:
        Base64 encoded string of the PNG image.
    """
    return take_screenshot()

@mcp.tool()
def window_list() -> str:
    """List all currently visible windows."""
    return list_windows()

@mcp.tool()
def window_manage(window_title: str, action: str) -> str:
    """
    Manage a specific window.
    Args:
        window_title: Title of window to control (fuzzy match)
        action: 'focus', 'minimize', 'maximize', 'restore', 'close'
    """
    return manage_window(window_title, action)

def main():
    parser = argparse.ArgumentParser(description="PC Control MCP Server")
    parser.add_argument("--transport", default="stdio", choices=["stdio", "sse"], help="Transport mode")
    args = parser.parse_args()

    mcp.run(transport=args.transport)

if __name__ == "__main__":
    main()
