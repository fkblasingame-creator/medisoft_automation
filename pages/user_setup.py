# pages/user_setup.py
import pyautogui
import time


# User definitions: (login_id, name, password, initials)
USERS = [
    ("1", "1", "11111111", "1"),
    ("2", "2", "22222222", "2"),
    ("3", "3", "33333333", "3"),
    ("4", "4", "44444444", "4"),
]


def _open_user_dialog():
    """Navigate to the Security Setup dialog."""
    time.sleep(2)
    pyautogui.hotkey("alt", "f")
    time.sleep(2)
    pyautogui.press("s")
    time.sleep(1)
    pyautogui.hotkey("alt", "n")
    time.sleep(1)


def _enter_user(login_id, name, password, initials, last=False):
    """Enter a single user into the form."""
    pyautogui.write(login_id)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)

    pyautogui.write(name)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)

    pyautogui.write(password)
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)

    pyautogui.write(password)      # Confirm password
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)

    pyautogui.write(initials)
    time.sleep(1)

    pyautogui.hotkey("alt", "s")   # Save
    time.sleep(1)

    print(f"  User created: {login_id}")

    if last:
        # Close the dialog after the last user
        pyautogui.hotkey("alt", "c")
        time.sleep(1)
        pyautogui.press("enter")
    else:
        # Open next user
        pyautogui.hotkey("alt", "n")
        time.sleep(1)


def create_users():
    """
    Create all users in Medisoft Security Setup.
    Called from main.py as: user_setup.create_users()
    """
    _open_user_dialog()

    for i, (login_id, name, password, initials) in enumerate(USERS):
        last = (i == len(USERS) - 1)
        _enter_user(login_id, name, password, initials, last=last)