import os
import subprocess
import shutil

def launch_application(app_name_or_path: str):
    """
    Launch an application by name or path.
    
    Args:
        app_name_or_path: Executable name (e.g. 'notepad') or full path.
    """
    try:
        # Try to find it in PATH if it's not a path
        if os.sep not in app_name_or_path:
            path = shutil.which(app_name_or_path)
            if path:
                app_name_or_path = path
        
        # os.startfile is Windows specific and very convenient as it detaches properly
        if hasattr(os, 'startfile'):
            os.startfile(app_name_or_path)
            return f"Launched: {app_name_or_path}"
        else:
            # Fallback for non-Windows (though this project is for PC/Windows)
            subprocess.Popen([app_name_or_path], shell=True)
            return f"Launched (subprocess): {app_name_or_path}"
            
    except Exception as e:
        return f"Error launching application: {str(e)}"
