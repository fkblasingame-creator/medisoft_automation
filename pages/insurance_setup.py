# pages/insurance_setup.py
import pyautogui
import time
from faker import Faker


def _generate_fake_insurance_data():
    """Generate fake insurance company data using Faker."""
    fake = Faker()
    return {
        "name":        fake.company(),
        "street":      fake.street_address(),
        "city":        fake.city(),
        "state":       fake.state_abbr(),
        "zip_code":    fake.zipcode(),
        "phone":       fake.phone_number(),
        "class_id":    str(fake.random_int(min=100, max=999)),
        "class_name":  fake.word().capitalize() + " " + fake.word().capitalize(),
        "description": fake.sentence(nb_words=8),
    }


def _open_insurance_dialog():
    """Navigate to the Insurance Carriers list and open a new entry."""
    time.sleep(3)
    pyautogui.hotkey("alt", "l")
    time.sleep(1)
    pyautogui.press("i")       # Insurance menu
    time.sleep(1)
    pyautogui.press("c")       # Insurance Carriers
    time.sleep(1)
    pyautogui.hotkey("alt", "n")
    time.sleep(3)              # Wait for new entry dialog


def _fill_main_tab(data):
    """Fill in the main tab fields of the insurance dialog."""
    pyautogui.press("tab", presses=2)   # Skip Code field (auto-generated)
    time.sleep(1)

    pyautogui.write(data["name"])       # Name
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(data["street"])     # Street
    pyautogui.press("tab", presses=2)
    time.sleep(0.5)

    pyautogui.write(data["zip_code"])   # Zip Code
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(data["city"])       # City
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(data["state"])      # State
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(data["phone"])      # Phone
    pyautogui.press("tab", presses=4)   # Skip extension and contact fields
    time.sleep(0.5)

    pyautogui.write("Plan Name")        # Plan Name
    pyautogui.press("tab")
    time.sleep(1)                       # Pause before opening Class ID dialog


def _fill_class_id(data):
    """Open the Class ID dialog and fill in class details."""
    pyautogui.press("f8")
    time.sleep(3)                           # Wait for Class ID dialog to open

    pyautogui.write(data["class_id"])       # Class ID
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(data["class_name"])     # Class Name
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(data["description"])    # Description
    pyautogui.press("tab")
    time.sleep(2)

    pyautogui.hotkey("alt", "s")            # Save class
    time.sleep(3)                           # Wait for dialog to close and return


def _fill_notes_and_options():
    """Fill in the Notes field and switch to the Options tab."""
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.write("Let me put your mind at ease, Jimmy")  # Notes
    time.sleep(1)

    pyautogui.press("tab", presses=6)
    time.sleep(2)

    # Switch to Options tab
    pyautogui.press("right")
    time.sleep(1)
    pyautogui.press("tab", presses=10)
    time.sleep(1)

    # Fill options dropdowns
    pyautogui.typewrite("i")   # Payment
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.typewrite("a")   # Adjustment
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.typewrite("w")   # Withhold
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.typewrite("d")   # Deductible
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.typewrite("t")   # Tax
    time.sleep(1)


def setup_insurance():
    """
    Create a new insurance carrier in Medisoft with fake data.
    Called from main.py as: insurance_setup.setup_insurance()
    """
    data = _generate_fake_insurance_data()

    _open_insurance_dialog()
    _fill_main_tab(data)
    _fill_class_id(data)
    _fill_notes_and_options()

    pyautogui.hotkey("alt", "s")   # Save and close
    time.sleep(2)

    print(f"  Insurance created: {data['name']}")