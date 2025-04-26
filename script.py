import mss
import keyboard
from PIL import Image
import pyperclipimg as pci
import time

def capture_and_copy():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Primary monitor
        width = monitor['width'] // 2
        height = monitor['height']
        left = monitor['left']
        top = monitor['top']

        # Define the region to capture
        region = {
            "top": top,
            "left": left,
            "width": width,
            "height": height
        }

        # Capture the region
        screenshot = sct.grab(region)

        # Convert to PIL Image
        img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)

        # Copy to clipboard
        pci.copy(img)
        print("Left half of the screen copied to clipboard.")


print("Press F6 to capture the left half of the screen. Press ESC to exit.")
while True:
    try:
        if keyboard.is_pressed('f6'):
            capture_and_copy()
            time.sleep(0.5)  # Prevent multiple captures on a single press
        elif keyboard.is_pressed('esc'):
            print("Exiting...")
            break
        time.sleep(0.1)
    except:
        break
