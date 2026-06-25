# pages/facility_setup.py
import pyautogui
import time
from faker import Faker


def _open_facility_dialog():
    """Open the Facility list and create a new entry. Standalone use only."""
    time.sleep(2)
    pyautogui.hotkey("alt", "l")
    time.sleep(1)
    pyautogui.press("e")           # Facilities
    time.sleep(1)
    pyautogui.hotkey("alt", "n")
    time.sleep(3)


def _fill_facility_fields(fake):
    """Fill in the facility form fields. Cursor starts on Code field."""
    pyautogui.press("tab")                              # Skip Code (auto-assigned)
    time.sleep(0.5)
    pyautogui.press("tab")                              # Skip Inactive checkbox

# Type: default to Facility
    pyautogui.press("tab")
    
    pyautogui.typewrite(fake.company())                 # Name
    pyautogui.press("tab")
    time.sleep(0.15)

    pyautogui.typewrite(fake.street_address())          # Street
    pyautogui.press("tab", presses=2)                   # Skip address line 2
    time.sleep(0.15)

    pyautogui.typewrite(fake.zipcode())                 # Zip Code
    pyautogui.press("tab")
    time.sleep(0.15)

    pyautogui.typewrite(fake.city())                    # City
    pyautogui.press("tab")
    time.sleep(0.15)

    pyautogui.typewrite(fake.state_abbr())              # State
    pyautogui.press("tab")
    time.sleep(0.15)

    pyautogui.typewrite(fake.word())                    # Extra 1
    pyautogui.press("tab")
    time.sleep(0.15)

    pyautogui.typewrite(fake.word())                    # Extra 2
    pyautogui.press("tab")
    time.sleep(0.15)

    pyautogui.press("tab")                              # Skip Purchased Services checkbox

    pyautogui.typewrite(fake.phone_number())            # Phone
    pyautogui.press("tab")
    time.sleep(0.15)

    pyautogui.typewrite(str(fake.random_int(min=101, max=999)))  # Extension
    pyautogui.press("tab")
    time.sleep(0.15)

    pyautogui.typewrite(fake.phone_number())            # Fax
    pyautogui.press("tab")
    time.sleep(0.15)

    pyautogui.typewrite(fake.phone_number())            # Cell
    pyautogui.press("tab")
    time.sleep(0.15)

    pyautogui.typewrite(fake.phone_number())            # Office
    pyautogui.press("tab")
    time.sleep(0.15)

    pyautogui.typewrite(fake.name())                    # Contact
    pyautogui.press("tab")
    time.sleep(0.15)

    pyautogui.typewrite(fake.email())                   # Email
    pyautogui.press("tab")
    time.sleep(1.5)

    # Select Facility ID tab
    pyautogui.press("tab", presses=4)
    pyautogui.press("right")
    time.sleep(0.5)

    # Add NPI
    pyautogui.hotkey("alt", "n")
    time.sleep(1)
    pyautogui.press("tab", presses=2)
    time.sleep(1)
    pyautogui.press("right", presses=2)
    time.sleep(0.5)
    pyautogui.typewrite("4958131232")                   # NPI
    time.sleep(0.5)

    pyautogui.hotkey("alt", "k")                       # OK
    time.sleep(1)


def _fill_facility_f8():
    """
    Fill facility form when opened via F8 from within a case.
    Cursor starts on Code field.
    """
    fake = Faker()
    _fill_facility_fields(fake)
    pyautogui.hotkey("alt", "s")
    time.sleep(2)
    pyautogui.press("enter")
    print("  Facility created via F8.")


def setup_facility():
    """
    Create a new facility in Medisoft.
    Called from main.py as: facility_setup.setup_facility()
    """
    fake = Faker()
    _open_facility_dialog()
    _fill_facility_fields(fake)
    pyautogui.hotkey("alt", "s")
    time.sleep(2)
    pyautogui.press("enter")
    print("  Facility created.")