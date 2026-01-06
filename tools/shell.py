import subprocess
import os

def execute_command(command: str, cwd: str = None) -> str:
    """
    Execute a shell command on the host machine.
    
    Args:
        command: The command to execute (e.g. 'dir', 'ipconfig', 'python script.py')
        cwd: Optional current working directory to execute in.
    """
    try:
        # Use shell=True to allow shell built-ins and flexible command execution
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd, 
            capture_output=True, 
            text=True,
            timeout=120 # 2 minute timeout for safety
        )
        output = result.stdout
        if result.stderr:
            output += f"\n[STDERR]\n{result.stderr}"
        
        # Add return code if failed
        if result.returncode != 0:
            output += f"\n[Process exited with code {result.returncode}]"
            
        return output.strip() or "[Command finished with no output]"
    except Exception as e:
        return f"Error executing command: {str(e)}"
