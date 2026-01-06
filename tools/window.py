import pygetwindow as gw
import json
import time

def list_windows() -> str:
    """
    List all visible windows with their titles.
    """
    try:
        windows = []
        for w in gw.getAllWindows():
            if w.visible and w.title:
                windows.append({
                    "title": w.title,
                    "id": w._hWnd, # Accessing internal handle if needed, or just title
                    "status": "active" if w.isActive else "inactive",
                    "state": "minimized" if w.isMinimized else "maximized" if w.isMaximized else "normal"
                })
        return json.dumps(windows, indent=2)
    except Exception as e:
        return f"Error listing windows: {str(e)}"

def manage_window(window_title: str, action: str) -> str:
    """
    Manage a specific window.
    
    Args:
        window_title: The title (or part of it) of the window to manage
        action: 'focus', 'minimize', 'maximize', 'restore', 'close'
    """
    try:
        # Find window (fuzzy match)
        target_window = None
        all_windows = gw.getAllWindows()
        
        # Exact match first
        for w in all_windows:
            if w.title == window_title:
                target_window = w
                break
        
        # Partial match if not found
        if not target_window:
            for w in all_windows:
                if window_title.lower() in w.title.lower():
                    target_window = w
                    break
        
        if not target_window:
            return f"Window not found matching: {window_title}"
            
        if action == "focus":
            target_window.activate()
            return f"Focused window: {target_window.title}"
        elif action == "minimize":
            target_window.minimize()
            return f"Minimized window: {target_window.title}"
        elif action == "maximize":
            target_window.maximize()
            return f"Maximized window: {target_window.title}"
        elif action == "restore":
            target_window.restore()
            return f"Restored window: {target_window.title}"
        elif action == "close":
            target_window.close()
            return f"Closed window: {target_window.title}"
        else:
            return f"Unknown action: {action}"
            
    except Exception as e:
        return f"Error managing window: {str(e)}"
