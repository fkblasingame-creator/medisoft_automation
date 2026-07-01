# pages/referring_provider_setup.py
import pyautogui
import time
from faker import Faker


def _open_referring_provider_dialog():
    """Navigate to the Referring Provider list and open a new entry."""
    time.sleep(3)
    pyautogui.hotkey("alt", "l")
    time.sleep(1)
    pyautogui.press("f")           # Referring Providers
    time.sleep(1)
    pyautogui.hotkey("alt", "n")
    time.sleep(3)                  # Wait for new entry dialog


def _fill_field(text):
    """Type text into the current field and tab to the next."""
    pyautogui.typewrite(str(text))
    pyautogui.press("tab")
    time.sleep(0.15)


def _fill_referring_provider(fake):
    """Fill in all fields for a referring provider."""
    _fill_field("")                                                          # Code (leave blank)
    pyautogui.hotkey("shift", "tab")                                        # Back to Last Name

    _fill_field(fake.last_name())                                           # Last Name
    _fill_field(fake.first_name())                                          # First Name
    _fill_field(fake.first_name())                                          # Middle Name
    _fill_field(fake.random_element(["MD", "DO", "RN", "NP", "PA"]))       # Credentials
    _fill_field(fake.street_address())                                      # Street
    pyautogui.press("tab")                                                  # Skip address line 2
    _fill_field(fake.zipcode())                                             # Zip Code
    _fill_field(fake.city())                                                # City
    _fill_field(fake.state_abbr())                                          # State
    _fill_field(fake.email())                                               # Email
    _fill_field(fake.phone_number())                                        # Office
    _fill_field(fake.phone_number())                                        # Fax
    _fill_field(fake.phone_number())                                        # Home
    _fill_field(fake.phone_number())                                        # Cell
    _fill_field(fake.bothify(text="????##"))                                # UPIN
    _fill_field(fake.word())                                                # Extra 1

    pyautogui.press("space")                                                # Medicare Participating checkbox
    pyautogui.press("tab")

    _fill_field(fake.bothify(text="???####"))                               # License Number
    _fill_field(fake.word())                                                # Extra 2

    # Specialty: pick random option from dropdown
    down_presses = fake.random_int(min=1, max=5)
    for _ in range(down_presses):
        pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("tab")

def _fill_referring_provider_f8():
    """
    Fill referring provider form when opened via F8 from within a case.
    Tab twice to reach Last Name field.
    """
    fake = Faker()

    pyautogui.press("tab", presses=2)                                       # Skip to Last Name

    _fill_field(fake.last_name())                                           # Last Name
    _fill_field(fake.first_name())                                          # First Name
    _fill_field(fake.first_name())                                          # Middle Name
    _fill_field(fake.random_element(["MD", "DO", "RN", "NP", "PA"]))       # Credentials
    _fill_field(fake.street_address())                                      # Street
    pyautogui.press("tab")                                                  # Skip address line 2
    _fill_field(fake.zipcode())                                             # Zip Code
    _fill_field(fake.city())                                                # City
    _fill_field(fake.state_abbr())                                          # State
    _fill_field(fake.email())                                               # Email
    _fill_field(fake.phone_number())                                        # Office
    _fill_field(fake.phone_number())                                        # Fax
    _fill_field(fake.phone_number())                                        # Home
    _fill_field(fake.phone_number())                                        # Cell
    _fill_field(fake.bothify(text="????##"))                                # UPIN
    _fill_field(fake.word())                                                # Extra 1

    pyautogui.press("space")                                                # Medicare Participating
    pyautogui.press("tab")

    _fill_field(fake.bothify(text="???####"))                               # License Number
    _fill_field(fake.word())                                                # Extra 2

    # Specialty dropdown
    down_presses = fake.random_int(min=1, max=5)
    for _ in range(down_presses):
        pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("tab")

    pyautogui.hotkey("alt", "s")                       # Save
    time.sleep(2)
    print("  Referring provider created via F8.")    
def setup_referring_provider():
    """
    Create a new referring provider in Medisoft with fake data.
    Called from main.py as: referring_provider_setup.setup_referring_provider()
    """
    fake = Faker()

    _open_referring_provider_dialog()
    _fill_referring_provider(fake)

    pyautogui.hotkey("alt", "s")   # Save
    time.sleep(2)

    print("  Referring provider created.")