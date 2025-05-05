import mss
import keyboard
from PIL import Image
import pyperclipimg as pci
import time
import pyautogui

def paste_and_enter_at_bottom_right():
    # 1) Define your base-resolution and the point you picked there
    BASE_WIDTH, BASE_HEIGHT = 2560, 1440   # your 2K monitor’s resolution
    base_x, base_y = 1754, 1250           # the Point you recorded

    # 2) Compute relative fractions
    rel_x = base_x / BASE_WIDTH
    rel_y = base_y / BASE_HEIGHT

    # 3) At runtime, get current screen size and scale
    screen_w, screen_h = pyautogui.size()
    x = int(screen_w * rel_x)
    y = int(screen_h * rel_y)
    
    pyautogui.moveTo(x, y)
    pyautogui.click()  # Focus the input box
    
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.press('enter')

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

        paste_and_enter_at_bottom_right()


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
