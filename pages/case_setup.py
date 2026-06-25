# pages/case_setup.py
import pyautogui
import time
import random
import string
from faker import Faker
from datetime import datetime
from pages import address_setup, referring_provider_setup


fake = Faker()


def safe_date_str(dt=None, fmt='%m/%d/%Y'):
    """Return a date string not later than today."""
    now = datetime.now()
    if dt is None:
        return now.strftime(fmt)
    try:
        if hasattr(dt, 'strftime'):
            return (min(dt, now)).strftime(fmt)
        parsed = datetime.strptime(str(dt), fmt)
        return (min(parsed, now)).strftime(fmt)
    except Exception:
        return now.strftime(fmt)


def _open_new_case():
    """Navigate to patient list and open a new case."""
    time.sleep(3)
    pyautogui.hotkey("alt", "l")
    time.sleep(3)
    pyautogui.press("p")
    time.sleep(3)
    pyautogui.press("tab", presses=3)
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.hotkey("alt", "n")   # Open new case
    time.sleep(7)


def _fill_personal_tab():
    """Fill in the Personal tab of the case."""
    # Description
    pyautogui.write(f"New Case {fake.name()}")
    pyautogui.press("tab", presses=2)

    # Global Coverage Until
    pyautogui.write("01012001")
    pyautogui.press("tab", presses=3)

    # Marital Status
    pyautogui.write("u")
    pyautogui.press("tab", presses=1)

    # Student Status
    pyautogui.write("n")
    pyautogui.press("tab", presses=1)
    time.sleep(2.5)

# Employer (F8 to create new)
    pyautogui.press("f8")
    time.sleep(3)
    address_setup._fill_employer_f8()
    pyautogui.hotkey("alt", "s")
    time.sleep(3)
    pyautogui.press("enter")

    # Employment Status
    pyautogui.write("u")
    pyautogui.press("enter")
    pyautogui.press("tab")

    # Location
    pyautogui.write("ok")
    pyautogui.press("tab")

    # Work Phone
    pyautogui.write(fake.numerify("##########"))
    time.sleep(1)


def setup_case():
    """
    Create a new case for the first patient in Medisoft.
    Called from main.py as: case_setup.setup_case()
    """
    _open_new_case()
    _fill_personal_tab()

    print("  Personal tab complete.")