# pages/practice_setup.py
import pyautogui
import time
import config

def create_new_practice():
    print("Clicking New to create a new practice...")
    pyautogui.hotkey('alt', 'n')
    time.sleep(3)
    
    print("Typing practice name...")
    pyautogui.write(config.PRACTICE_NAME, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.5)
    
    print("Typing folder name...")
    pyautogui.write(config.FOLDER_NAME, interval=0.1)
    time.sleep(0.5)
    
    print("Clicking Create...")
    pyautogui.hotkey('alt', 'r')
    time.sleep(3)
    
    print("Confirming directory creation...")
    pyautogui.hotkey('alt', 'y')
    time.sleep(15)
    print("Practice created!")
    
def login():
    print("Logging in...")
    pyautogui.write(config.USERNAME, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.5)
    
    pyautogui.write(config.PASSWORD, interval=0.1)
    time.sleep(0.5)
    
    pyautogui.press('enter')
    time.sleep(15)  # Wait for Medisoft to load the new practice
    print("Logged in successfully!")
    time.sleep(1)
    pyautogui.press('enter')
    
def fill_practice_info():
    print("Filling in practice information...")
    time.sleep(3)  # Wait for form to fully load
    
    pyautogui.write(config.PRACTICE_NAME, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    
       
    pyautogui.write(config.STREET_ADDRESS, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    pyautogui.press('tab')
    time.sleep(0.3)
     
    pyautogui.write(config.ZIP, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    
    pyautogui.write(config.CITY, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    
    pyautogui.write(config.STATE, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    
    pyautogui.write(config.PHONE, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    
    pyautogui.write(config.EXTENSION, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    
    pyautogui.write(config.ALT_PHONE, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    
    pyautogui.write(config.EMAIL, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    
    pyautogui.write(config.INITIAL, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    
    pyautogui.write(config.FAX, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    
    # Two extra tabs before Extra fields
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(0.3)
    
    pyautogui.write(config.EXTRA1, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    
    pyautogui.write(config.EXTRA2, interval=0.1)
    pyautogui.press('tab')
    time.sleep(0.3)
    
    print("Saving practice info...")
    pyautogui.hotkey('alt', 's')
    time.sleep(3)
    print("Practice info saved!")

if __name__ == "__main__":
    fill_practice_info()    