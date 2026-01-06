import psutil
import shutil
import json

def get_system_status() -> str:
    """
    Get current system status including CPU, Memory, and Disk usage.
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    
    memory = psutil.virtual_memory()
    mem_total_gb = round(memory.total / (1024**3), 2)
    mem_used_gb = round(memory.used / (1024**3), 2)
    mem_percent = memory.percent
    
    # Disk usage for all mounted drives
    disks = []
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disks.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "total_gb": round(usage.total / (1024**3), 2),
                "free_gb": round(usage.free / (1024**3), 2),
                "percent_used": usage.percent
            })
        except PermissionError:
            continue
            
    # Network statistics
    net_io = psutil.net_io_counters()
    network = {
        "bytes_sent_mb": round(net_io.bytes_sent / (1024**2), 2),
        "bytes_recv_mb": round(net_io.bytes_recv / (1024**2), 2)
    }
    
    battery = psutil.sensors_battery()
    battery_info = "N/A"
    if battery:
        battery_info = f"{battery.percent}% ({'Plugged In' if battery.power_plugged else 'On Battery'})"

    status = {
        "cpu_usage_percent": cpu_percent,
        "memory": {
            "total_gb": mem_total_gb,
            "used_gb": mem_used_gb,
            "percent": mem_percent
        },
        "disks": disks,
        "network": network,
        "battery": battery_info
    }
    
    return json.dumps(status, indent=2)
