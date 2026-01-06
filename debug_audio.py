from pycaw.pycaw import AudioUtilities
import comtypes

try:
    comtypes.CoInitialize()
    devices = AudioUtilities.GetSpeakers()
    print(f"Type: {type(devices)}")
    print(f"Dir: {dir(devices)}")
except Exception as e:
    print(f"Error: {e}")
