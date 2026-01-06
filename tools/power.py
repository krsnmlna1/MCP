import os
import subprocess

def manage_power(action: str):
    """
    Perform power management actions.
    
    Args:
        action: 'shutdown', 'restart', 'sleep', 'lock', 'abort'
    """
    try:
        if action == "lock":
            # Lock workstation
            os.system("rundll32.exe user32.dll,LockWorkStation")
            return "Workstation locked."
            
        elif action == "sleep":
            # Hybrid sleep/hibernate usually preferred, or standard sleep
            # providing simple standard sleep command
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            return "System going to sleep..."
            
        elif action == "shutdown":
            # Shutdown in 60 seconds with comment
            os.system("shutdown /s /t 60 /c \"AI Agent requested shutdown\"")
            return "Shutdown scheduled in 60 seconds. Use action='abort' to cancel."
            
        elif action == "restart":
            os.system("shutdown /r /t 60 /c \"AI Agent requested restart\"")
            return "Restart scheduled in 60 seconds. Use action='abort' to cancel."
            
        elif action == "abort":
            os.system("shutdown /a")
            return "Shutdown/Restart aborted."
            
        else:
            return f"Unknown action: {action}"
            
    except Exception as e:
        return f"Error executing power action: {str(e)}"
