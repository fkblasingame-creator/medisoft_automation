# pages/icd10_setup.py
import icd10
import pyautogui
import time
import random


def _get_random_billable_code():
    """Return a random billable ICD-10 entry."""
    billable_codes = [code for code in icd10.codes if icd10.find(code).billable]
    selected_code = random.choice(billable_codes)
    return icd10.find(selected_code)


def _enter_icd10_code(entry):
    """Type a single ICD-10 code and description into the open dialog."""
    pyautogui.write(entry.code)
    pyautogui.press("tab")
    pyautogui.write(entry.description)
    pyautogui.press("tab", presses=4, interval=0.3)
    pyautogui.press("enter")
    pyautogui.press("enter")
    print(f"  Entered: {entry.code}  {entry.description}")


def _save_and_new():
    """Save the current entry and open a new one."""
    time.sleep(1)
    pyautogui.hotkey("alt", "s")
    time.sleep(1)
    pyautogui.hotkey("alt", "n")
    time.sleep(5)  # Allow time for the new dialog to open


def setup_icd10_codes(count=3):
    """
    Open the ICD-10 dialog in Medisoft and enter `count` random billable codes.
    Called from main.py as: icd10_setup.setup_icd10_codes(count=3)
    """
    # Open Lists menu and navigate to ICD-10 dialog
    time.sleep(2)
    pyautogui.hotkey("alt", "l")
    time.sleep(1)
    pyautogui.press("d")
    time.sleep(1)
    pyautogui.hotkey("alt", "n")
    time.sleep(5)  # Wait for new entry dialog to open

    for i in range(count):
        entry = _get_random_billable_code()
        _enter_icd10_code(entry)

        if i < count - 1:
            # More codes to enter — save and open next
            _save_and_new()
        else:
            # Last code — save and close
            time.sleep(1)
            pyautogui.hotkey("alt", "s")
            time.sleep(1)
            pyautogui.hotkey("alt", "c")