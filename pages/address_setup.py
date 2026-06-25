# pages/address_setup.py
import pyautogui
import time
import random
from faker import Faker


COMPANY_PREFIXES = [
    "Tech", "Blue", "Green", "Quantum", "Global", "Smart", "Next", "Bright", "Future", "Dynamic",
    "Prime", "Urban", "Cloud", "Nova", "Peak"
]

COMPANY_SUFFIXES = [
    "Solutions", "Systems", "Networks", "Labs", "Industries", "Works", "Partners", "Vision", "Dynamics", "Innovations"
]


def _generate_company_name():
    """Generate a random fake company name."""
    return f"{random.choice(COMPANY_PREFIXES)} {random.choice(COMPANY_SUFFIXES)}"


def _open_address_dialog():
    """Open the Address list and create a new entry. Standalone use only."""
    time.sleep(4)
    pyautogui.hotkey("alt", "l")
    time.sleep(1)
    pyautogui.press("a")           # Addresses
    time.sleep(1)
    pyautogui.hotkey("alt", "n")
    time.sleep(3)


def _fill_address_fields(address_type):
    """
    Fill address form opened via Lists menu.
    Cursor starts on Code field — tabs to Name first.
    """
    fake = Faker()
    company_name = _generate_company_name()

    pyautogui.press("tab", presses=2)                   # Skip Code to Name
    time.sleep(0.5)

    pyautogui.write(company_name)                       # Name
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(fake.street_address())              # Street
    pyautogui.press("tab", presses=2)                   # Skip address line 2
    time.sleep(0.5)

    zip_code = "{:05d}".format(random.randint(0, 99999))
    pyautogui.write(zip_code)                           # Zip Code
    time.sleep(0.5)
    pyautogui.press("tab")

    pyautogui.write(fake.city())                        # City
    pyautogui.press("tab")

    pyautogui.write(fake.state_abbr())                  # State
    pyautogui.press("tab", presses=2)
    time.sleep(0.5)

    # Set Type dropdown
    type_keys = {
        "attorney":      "a",
        "employer":      "e",
        "miscellaneous": "m",
        "referral":      "r",
    }
    pyautogui.press(type_keys[address_type])
    time.sleep(0.5)
    pyautogui.press("tab")

    pyautogui.write(fake.msisdn()[:10])                 # Phone
    pyautogui.press("tab")

    pyautogui.write(str(random.randint(100, 999)))      # Extension
    pyautogui.press("tab")

    pyautogui.write(fake.msisdn()[:10])                 # Fax
    pyautogui.press("tab")

    pyautogui.write(fake.msisdn()[:10])                 # Cell
    pyautogui.press("tab")

    pyautogui.write(fake.msisdn()[:10])                 # Office
    pyautogui.press("tab")

    pyautogui.write(fake.name())                        # Contact
    pyautogui.press("tab")

    pyautogui.write(fake.email())                       # Email
    pyautogui.press("tab")

    pyautogui.write(fake.word())                        # Extra 1
    pyautogui.press("tab")

    pyautogui.write(fake.word())                        # Extra 2
    pyautogui.press("tab")

    print(f"  Address filled: {company_name} ({address_type})")


def _fill_employer_f8():
    """
    Fill employer address form when opened via F8 from within a case.
    Cursor starts directly on Name field — no tabs needed to skip Code.
    Always creates an Employer type address.
    """
    fake = Faker()
    company_name = _generate_company_name()

    pyautogui.write(company_name)                       # Name
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(fake.street_address())              # Street
    pyautogui.press("tab", presses=2)                   # Skip address line 2
    time.sleep(0.5)

    zip_code = "{:05d}".format(random.randint(0, 99999))
    pyautogui.write(zip_code)                           # Zip Code
    time.sleep(0.5)
    pyautogui.press("tab")

    pyautogui.write(fake.city())                        # City
    pyautogui.press("tab")

    pyautogui.write(fake.state_abbr())                  # State
    pyautogui.press("tab", presses=2)
    time.sleep(0.5)

    pyautogui.press("e")                                # Type = Employer
    time.sleep(0.5)
    pyautogui.press("tab")

    pyautogui.write(fake.msisdn()[:10])                 # Phone
    pyautogui.press("tab")

    pyautogui.write(str(random.randint(100, 999)))      # Extension
    pyautogui.press("tab")

    pyautogui.write(fake.msisdn()[:10])                 # Fax
    pyautogui.press("tab")

    pyautogui.write(fake.msisdn()[:10])                 # Cell
    pyautogui.press("tab")

    pyautogui.write(fake.msisdn()[:10])                 # Office
    pyautogui.press("tab")

    pyautogui.write(fake.name())                        # Contact
    pyautogui.press("tab")

    pyautogui.write(fake.email())                       # Email
    pyautogui.press("tab")

    pyautogui.write(fake.word())                        # Extra 1
    pyautogui.press("tab")

    pyautogui.write(fake.word())                        # Extra 2
    pyautogui.press("tab")

    print(f"  Employer created: {company_name}")


# --- Standalone creation functions (use Lists menu navigation) ---

def setup_attorney():
    """Create a new Attorney address entry from the Lists menu."""
    _open_address_dialog()
    _fill_address_fields("attorney")
    pyautogui.hotkey("alt", "s")
    time.sleep(2)


def setup_employer():
    """Create a new Employer address entry from the Lists menu."""
    _open_address_dialog()
    _fill_address_fields("employer")
    pyautogui.hotkey("alt", "s")
    time.sleep(2)


def setup_miscellaneous():
    """Create a new Miscellaneous address entry from the Lists menu."""
    _open_address_dialog()
    _fill_address_fields("miscellaneous")
    pyautogui.hotkey("alt", "s")
    time.sleep(2)


def setup_referral():
    """Create a new Referral Source address entry from the Lists menu."""
    _open_address_dialog()
    _fill_address_fields("referral")
    pyautogui.hotkey("alt", "s")
    time.sleep(2)