import time
import json
import base64
import os
from tools.system import get_system_status
from tools.processes import get_process_list
from tools.screen import take_screenshot
from tools.window import list_windows, manage_window
from tools.app_launcher import launch_application

def verify():
    print("--- 1. Testing System Status ---")
    status = json.loads(get_system_status())
    print(f"Network keys present: {'network' in status}")
    print(f"Disks keys present: {'disks' in status}")
    print(f"Disks found: {len(status.get('disks', []))}")
    
    print("\n--- 2. Testing Process List ---")
    procs = json.loads(get_process_list(limit=3))
    print(f"Top 3 processes: {[p['name'] for p in procs]}")
    
    print("\n--- 3. Testing Screenshot ---")
    img_b64 = take_screenshot()
    if img_b64.startswith("Error"):
        print(f"Screenshot FAILED: {img_b64}")
    else:
        try:
            # check if valid base64
            base64.b64decode(img_b64)
            print(f"Screenshot SUCCESS (Length: {len(img_b64)})")
            # Save for inspection if needed
            # with open("test_screen.png", "wb") as f:
            #     f.write(base64.b64decode(img_b64))
        except Exception as e:
            print(f"Screenshot Invalid Base64: {e}")

    print("\n--- 4. Testing Window Management ---")
    print("Launching Notepad...")
    launch_application("notepad.exe")
    time.sleep(2) # Wait for it to open
    
    windows = json.loads(list_windows())
    notepad_found = False
    for w in windows:
        if "notepad" in w['title'].lower():
            print(f"Found Notepad: {w['title']}")
            notepad_found = True
            break
            
    if notepad_found:
        print("Minimizing Notepad...")
        print(manage_window("Notepad", "minimize"))
        time.sleep(1)
        print("Restoring Notepad...")
        print(manage_window("Notepad", "restore"))
        time.sleep(1)
        print("Closing Notepad...")
        print(manage_window("Notepad", "close"))
    else:
        print("FAILED to find Notepad window")

if __name__ == "__main__":
    verify()
