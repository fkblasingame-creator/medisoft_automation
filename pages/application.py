# pages/application.py
import subprocess
import pyautogui
import time
import config

def wait_for_screen(image_path, timeout=30):
    """Waits until a specific screen/element appears before continuing."""
    print(f"Waiting for {image_path}...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.5)
            if location is not None:
                print(f"Found {image_path}!")
                return location
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.5)
    raise TimeoutError(f"Timed out waiting for {image_path}")

def launch_medisoft():
    print("Launching Medisoft...")
    subprocess.Popen(config.MEDISOFT_PATH)
    
    # Give Medisoft time to load on VM
    print("Waiting for Medisoft to load...")
    time.sleep(15)
    print("Medisoft should be ready!")
    
    # Hit Ctrl+C to open Open Practice dialog
    pyautogui.hotkey('alt', 'c')
    time.sleep(3)
    print("Open Practice dialog should be open!")