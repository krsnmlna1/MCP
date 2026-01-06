from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import math

def get_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    # Check for new pycaw wrapper (2024+)
    if hasattr(devices, 'EndpointVolume'):
        return devices.EndpointVolume
    
    # Legacy pycaw (raw COM pointer)
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return interface.QueryInterface(IAudioEndpointVolume)

def manage_volume(action: str, level: int = None):
    """
    Control system audio volume.
    
    Args:
        action: 'set', 'get', 'mute', 'unmute'
        level: 0-100 (required for 'set')
    """
    try:
        # Initialize COM library for the current thread
        import comtypes
        comtypes.CoInitialize()
        
        volume = get_volume_interface()
        
        if action == "get":
            current = volume.GetMasterVolumeLevelScalar()
            is_muted = volume.GetMute()
            return f"Current Volume: {int(current * 100)}% (Muted: {bool(is_muted)})"
            
        elif action == "set":
            if level is None:
                return "Error: 'level' is required for action 'set'"
            # Ensure level is 0-100
            level = max(0, min(100, level))
            scalar = level / 100.0
            volume.SetMasterVolumeLevelScalar(scalar, None)
            return f"Volume set to {level}%"
            
        elif action == "mute":
            volume.SetMute(1, None)
            return "System muted"
            
        elif action == "unmute":
            volume.SetMute(0, None)
            return "System unmuted"
            
        else:
            return f"Unknown action: {action}"
            
    except Exception as e:
        return f"Error controlling volume: {str(e)}"
