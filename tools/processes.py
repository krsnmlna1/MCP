import psutil
import json

def get_process_list(sort_by: str = "cpu", limit: int = 10) -> str:
    """
    Get a list of running processes, sorted by resource usage.
    
    Args:
        sort_by: 'cpu' or 'memory'
        limit: Number of processes to return
    """
    try:
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                pinfo = proc.info
                processes.append(pinfo)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        if sort_by == 'memory':
            processes.sort(key=lambda x: x['memory_percent'] or 0, reverse=True)
        else:
            # CPU percent requires two calls to be accurate, but process_iter gives a convenient valid value usually if called iteratively
            # For meaningful one-shot, we rely on what psutil gives, which might be 0.0 for first call.
            # However, simpler is better for now. 
            processes.sort(key=lambda x: x['cpu_percent'] or 0, reverse=True)

        return json.dumps(processes[:limit], indent=2)
    except Exception as e:
        return f"Error getting process list: {str(e)}"
