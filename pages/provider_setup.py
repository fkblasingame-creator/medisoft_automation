# pages/provider_setup.py
import pyautogui
import time
import random
import config
from faker import Faker

fake = Faker()

def generate_npi():
    digits = [random.randint(1,9)] + [random.randint(0,9) for _ in range(8)]
    def luhn_checksum(digits):
        total = 0
        reverse_digits = digits[::-1]
        for i, d in enumerate(reverse_digits):
            if i % 2 == 0:
                total += d
            else:
                doubled = d * 2
                total += doubled if doubled < 10 else doubled - 9
        return (10 - (total % 10)) % 10
    check_digit = luhn_checksum(digits)
    digits.append(check_digit)
    return ''.join(map(str, digits))

def fill_field(text):
    pyautogui.typewrite(str(text))
    pyautogui.press('tab')
    time.sleep(0.2)

def create_provider():
    print("Navigating to Provider list...")
    pyautogui.hotkey('alt', 'l')
    time.sleep(0.5)
    pyautogui.typewrite('r')
    time.sleep(0.5)
    pyautogui.typewrite('v')
    time.sleep(0.5)
    
    print("Creating new provider...")
    pyautogui.hotkey('alt', 'n')
    time.sleep(2)
    
    print("Filling in Address tab...")
    fill_field(config.PROVIDER_LAST_NAME)
    fill_field(config.PROVIDER_FIRST_NAME)
    fill_field(config.PROVIDER_MIDDLE_NAME)
    fill_field(config.PROVIDER_CREDENTIALS)
    
    fill_field(config.PROVIDER_STREET)
    pyautogui.press('tab')  # Skip street line 2
    
    fill_field(config.PROVIDER_ZIP)
    fill_field(config.PROVIDER_CITY)
    fill_field(config.PROVIDER_STATE)
    fill_field(config.PROVIDER_EMAIL)
    fill_field(config.PROVIDER_OFFICE_PHONE)
    fill_field(config.PROVIDER_HOME_PHONE)
    fill_field(config.PROVIDER_FAX)
    fill_field(config.PROVIDER_CELL_PHONE)
    
    pyautogui.press('space')  # Signature On File
    pyautogui.press('tab')
    time.sleep(0.5)
    
    pyautogui.press('space')  # Medicare Participating
    pyautogui.press('tab')
    time.sleep(0.5)
    
    fill_field(fake.date_between(start_date='-5y', end_date='today'))  # Signature Date - past dates only
    time.sleep(0.5)
    
    fill_field(config.PROVIDER_LICENSE)
    time.sleep(0.5)
    
    pyautogui.press('tab', presses=6)  # Navigate to Provider IDs tab
    time.sleep(1.5)  # Stop and let Medisoft catch up
    
    pyautogui.press('right')
    time.sleep(0.5)
    pyautogui.press('right')
    time.sleep(1)
    
    print("Filling in Provider IDs tab...")
    pyautogui.hotkey('alt', 'n')
    time.sleep(2)
    
    pyautogui.press('tab', presses=2)
    pyautogui.press('right')
    pyautogui.press('tab', presses=1)
    pyautogui.press('right', presses=2)
    time.sleep(0.5)
    
    npi = generate_npi()
    print(f"Generated NPI: {npi}")
    pyautogui.write(npi)
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')
    time.sleep(1.5)
    
    print("Saving provider...")
    pyautogui.hotkey('alt', 's')
    print("Provider saved!")

if __name__ == "__main__":
    create_provider()
def _fill_provider_f8():
    """
    Fill provider form when opened via F8 from within a case.
    Uses Faker for random data. Tab twice to reach Last Name field.
    """
    fake_local = Faker()

    pyautogui.press("tab", presses=2)                   # Skip to Last Name

    fill_field(fake_local.last_name())                  # Last Name
    fill_field(fake_local.first_name())                 # First Name
    fill_field(fake_local.first_name())                 # Middle Name
    fill_field(fake_local.random_element(["MD", "DO", "RN", "NP", "PA"]))  # Credentials

    fill_field(fake_local.street_address())             # Street
    pyautogui.press("tab")                              # Skip street line 2

    fill_field(fake_local.zipcode())                    # Zip
    fill_field(fake_local.city())                       # City
    fill_field(fake_local.state_abbr())                 # State
    fill_field(fake_local.email())                      # Email
    fill_field(fake_local.phone_number())               # Office
    fill_field(fake_local.phone_number())               # Fax
    fill_field(fake_local.phone_number())               # Home
    fill_field(fake_local.phone_number())               # Cell

    pyautogui.press("space")                            # Signature On File
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.press("space")                            # Medicare Participating
    pyautogui.press("tab")
    time.sleep(0.5)

    fill_field(fake_local.date_between(start_date="-5y", end_date="today"))  # Signature Date

    fill_field(fake_local.bothify(text="???####"))      # License Number

    # Navigate to Provider IDs tab
    pyautogui.press("tab", presses=6)
    time.sleep(1.5)
    pyautogui.press("right", presses=2)
    time.sleep(1)

    # Add NPI
    pyautogui.hotkey("alt", "n")
    time.sleep(2)
    pyautogui.press("tab", presses=2)
    pyautogui.press("right")
    pyautogui.press("tab")
    pyautogui.press("right", presses=2)
    time.sleep(0.5)

    npi = generate_npi()
    pyautogui.write(npi)
    pyautogui.press("enter")
    pyautogui.hotkey("alt", "k")
    time.sleep(1.5)

    pyautogui.hotkey("alt", "s")                       # Save
    time.sleep(2)
    print("  Provider created via F8.")
