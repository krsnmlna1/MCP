import mss
import mss.tools
import base64
import os
import time

def take_screenshot() -> str:
    """
    Take a screenshot of the primary monitor.
    Returns:
        A base64 encoded string of the PNG image.
    """
    try:
        with mss.mss() as sct:
            # Grab the primary monitor (monitor 1)
            monitor = sct.monitors[1]
            
            # Grab the data
            sct_img = sct.grab(monitor)
            
            # Save to specific path temporarily to read back as base64
            # We use a temp file in the current directory or temp dir
            temp_filename = f"screenshot_{int(time.time())}.png"
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=temp_filename)
            
            try:
                with open(temp_filename, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                
                # Clean up
                os.remove(temp_filename)
                
                return encoded_string
            except Exception as read_err:
                if os.path.exists(temp_filename):
                    os.remove(temp_filename)
                raise read_err
                
    except Exception as e:
        return f"Error taking screenshot: {str(e)}"
