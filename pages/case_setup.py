# pages/case_setup.py
import pyautogui
import time
import random
import string
from faker import Faker
from datetime import datetime
from pages import address_setup, referring_provider_setup, provider_setup, facility_setup


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

def _fill_account_tab():
    """Fill in the Account tab of the case."""
    pyautogui.hotkey("alt", "a")    # Switch to Account tab
    time.sleep(3)

    # Assigned Provider (focus is here when tab opens)
    pyautogui.press("f8")
    time.sleep(3)
    provider_setup._fill_provider_f8()
    time.sleep(1)
    pyautogui.press("tab")

    # Referring Provider
    pyautogui.press("f8")
    time.sleep(3)
    referring_provider_setup._fill_referring_provider_f8()
    time.sleep(1)
    pyautogui.press("tab")

    # Supervising Provider
    pyautogui.press("f8")
    time.sleep(3)
    provider_setup._fill_provider_f8()
    time.sleep(1)
    pyautogui.press("tab")

# Referral Source
    pyautogui.press("f8")
    time.sleep(3)
    address_setup._fill_referral_f8()
    time.sleep(1)
    pyautogui.press("tab")

    # Attorney
    pyautogui.press("f8")
    time.sleep(3)
    address_setup._fill_attorney_f8()
    time.sleep(1)
    pyautogui.press("tab")

    # Facility
    pyautogui.press("f8")
    time.sleep(3)
    facility_setup._fill_facility_f8()
    time.sleep(1)

    # Bottom fields
    pyautogui.press("tab", presses=3)  # Skip to Other Arrangements
    pyautogui.write(fake.word())        # Other Arrangements
    pyautogui.press("tab", presses=2)  # Skip to Authorization Number
    pyautogui.write(fake.bothify(text="AUTH###??"))  # Authorization Number
    pyautogui.press("tab", presses=2)
    pyautogui.write(str(fake.random_int(min=1, max=99)))  # Authorized Visits
    pyautogui.press("tab")
    pyautogui.write(fake.bothify(text="ID###"))            # ID
    pyautogui.press("tab")
    pyautogui.write(str(fake.random_int(min=1, max=99)))  # Last Visit Number
    time.sleep(1)

    print("  Account tab complete.")
def _fill_diagnosis_popup():
    """Fill in a single diagnosis code popup."""
    time.sleep(1.2)

    pyautogui.typewrite(fake.bothify(text="D??#"))          # Code
    pyautogui.press("tab")

    pyautogui.typewrite(fake.sentence(nb_words=4))          # Description
    pyautogui.press("tab")

    pyautogui.typewrite(fake.bothify(text="###.#"))         # ICD-9 Code
    pyautogui.press("tab", presses=2)                       # Skip ICD-9 extra field

    pyautogui.typewrite(fake.sentence(nb_words=3))          # ICD-9 Description
    pyautogui.press("tab")

    pyautogui.typewrite(fake.bothify(text="?##.###"))       # ICD-10 Code
    pyautogui.press("tab", presses=2)                       # Skip ICD-10 extra field

    pyautogui.typewrite(fake.sentence(nb_words=3))          # ICD-10 Description
    pyautogui.press("tab")

    if fake.boolean():
        pyautogui.press("space")                            # HIPAA Approved (random)
    pyautogui.press("tab")

    pyautogui.hotkey("alt", "s")                           # Save
    time.sleep(2.2)


def _fill_diagnosis_tab():
    """Fill in the Diagnosis tab with 4 diagnosis codes."""
    pyautogui.hotkey("alt", "d")    # Switch to Diagnosis tab
    time.sleep(3)

    for i in range(4):
        pyautogui.press("f8")           # Open diagnosis popup
        _fill_diagnosis_popup()         # Fill and save

        if i < 3:
            pyautogui.press("tab")      # Move to next diagnosis field
            time.sleep(0.2)

    print("  Diagnosis tab complete.")
def _fill_insurance_f8():
    """Fill insurance carrier form opened via F8 from within a case."""
    fake_local = Faker()
    pyautogui.press("tab", presses=2)                   # Skip Code to Name
    time.sleep(0.5)
    name = fake_local.company()
    street = fake_local.street_address()
    city = fake_local.city()
    state = fake_local.state_abbr()
    zip_code = fake_local.zipcode()
    phone = fake_local.phone_number()
    class_id = str(fake_local.random_int(min=100, max=999))
    class_name = fake_local.word().capitalize() + " " + fake_local.word().capitalize()
    description = fake_local.sentence(nb_words=8)

    pyautogui.write(name)                               # Name
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(street)                             # Street
    pyautogui.press("tab", presses=2)                   # Skip address line 2

    pyautogui.write(zip_code)                           # Zip Code
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(city)                               # City
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(state)                              # State
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(phone)                              # Phone
    pyautogui.press("tab", presses=4)                   # Skip extension, contact fields
    time.sleep(0.5)

    pyautogui.write("Plan Name")                        # Plan Name
    pyautogui.press("tab")

    # Class ID (F8)
    pyautogui.press("f8")
    time.sleep(2)
    pyautogui.write(class_id)                           # Class ID
    pyautogui.press("tab")
    pyautogui.write(class_name)                         # Class Name
    pyautogui.press("tab")
    pyautogui.write(description)                        # Description
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.hotkey("alt", "s")                       # Save class
    time.sleep(2)

    pyautogui.press("tab")
    pyautogui.write("This is a Note and only a Note")  # Notes
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("tab", presses=5)
    time.sleep(2)

    pyautogui.hotkey("alt", "s")                       # Save insurance
    time.sleep(2)
    print("  Insurance created via F8.")


def _fill_policy_fields():
    """Fill in the policy number, group, and other fields after insurance is selected."""
    pyautogui.press("tab", presses=3)
    time.sleep(2.5)

    policy_number = "".join(random.choices(string.ascii_uppercase + string.digits, k=14))
    pyautogui.write(policy_number)                      # Policy Number
    pyautogui.press("tab")

    group_number = str(random.randint(100000000, 999999999))
    pyautogui.write(group_number)                       # Group Number
    pyautogui.press("tab")
    time.sleep(1.5)

    pyautogui.write(fake.company())                     # Group Name
    pyautogui.press("tab")
    time.sleep(1.5)

    claim_number = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    pyautogui.write(claim_number)                       # Claim Number
    pyautogui.press("tab")
    time.sleep(1.5)

    pyautogui.write("01012025")                         # Start Date
    pyautogui.press("tab", presses=4)
    time.sleep(1.5)

    pyautogui.press("space")                            # Checkbox
    pyautogui.press("tab", presses=4)

    pyautogui.write("25")                               # Copay
    pyautogui.press("tab")

    auth_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    pyautogui.write(f"AUT#{auth_code}")                 # Treatment Auth
    time.sleep(1)


def _fill_policy_tab(policy_number):
    """
    Fill in a Policy tab (1, 2, or 3).
    policy_number: 1, 2, or 3
    """
    hotkeys = {1: "1", 2: "2", 3: "3"}
    pyautogui.hotkey("alt", hotkeys[policy_number])    # Switch to correct policy tab
    time.sleep(3)

    # Insurance (F8 to create new)
    pyautogui.press("f8")
    time.sleep(2)
    _fill_insurance_f8()
    time.sleep(1)
    
    _fill_policy_fields()
    print(f"  Policy {policy_number} tab complete.")

def _fill_miscellaneous_tab():
    """Fill in the Miscellaneous tab of the case."""
    pyautogui.hotkey("alt", "m")    # Switch to Miscellaneous tab
    time.sleep(3)

    pyautogui.press("tab")
    pyautogui.write("120")                              # Lab Charges
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("Medicare Use Only")                # Local Use A
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("Chiropractor = 0")                 # Local Use B
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("5876")                             # Indicator
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(safe_date_str())                    # Referral Date
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(safe_date_str())                    # Prescription Date
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("8675309")                          # Prior Auth Number
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("Extra 1")                          # Extra 1
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("Extra 2")                          # Extra 2
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("Extra 3")                          # Extra 3
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("Extra 4")                          # Extra 4
    pyautogui.press("tab")
    time.sleep(0.5)

    print("  Miscellaneous tab complete.")

def _fill_medicaid_tab():
    """Fill in the Medicaid and Tricare tab of the case."""
    pyautogui.hotkey("alt", "n")    # Switch to Medicaid and Tricare tab
    time.sleep(3)

    pyautogui.press("tab", presses=2)                   # Skip to first field

    # Regression numbers (2)
    for _ in range(2):
        number = str(random.randint(10**11, 10**12 - 1))
        pyautogui.write(number)
        pyautogui.press("tab")
        time.sleep(0.5)

    pyautogui.write("Exception code is NO")             # SAEC
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("s")                                # Special Program Code
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("a")                                # EPSDT
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("n")                                # EPSDT
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("s")                                # EPSDT
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("n")                                # Non Availability
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("c")                                # Branch
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("m")                                # Sponsor
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("a")                                # Special Program
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("e")                                # EPSDT
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write(safe_date_str())                    # Referral Date
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.hotkey("alt", "o")                       # Move to next tab
    print("  Medicaid and Tricare tab complete.")

def _fill_comment_tab():
    """Fill in the Comment tab of the case."""
   
    time.sleep(3)

    pyautogui.write("Blue lips are a sign of hypothermia")     # Allergies
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("a")                                        # Note Reference Code
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("It would have been ok if it was just a sports bar")  # Note
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("f")                                        # Contact Type
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("12000")                                    # Contact Amount
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("a")                                        # Percent
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("code")                                     # Code
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("33")                                       # Percent
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("32a")                                      # Percent
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("When a true genius appears in the world, you may know him by this sign; that the dunces are all in confederacy against him.")  # Comment
    pyautogui.press("tab")
    time.sleep(1.5)

    print("  Comment tab complete.")

def _fill_edi_tab():
    """Fill in the EDI tab of the case."""
    pyautogui.hotkey("alt", "i")    # Switch to EDI tab
    time.sleep(3)

    pyautogui.write("5677")                             # Care Plan Number
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("a")                                # Assignment In
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("7")                                # Hospice
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("n")                                # Timely Filing Indicator
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("1")                                # CLIA
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.press("tab")                              # Skip empty field
    time.sleep(0.5)

    pyautogui.write("code")                             # Memory
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("33")                               # Referral Access
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("32a")                              # Demo Code
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("2987479")                          # IDE Number
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("Ill")                              # Condition Indicator
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.write("1")                                # Code Category
    pyautogui.press("tab")
    time.sleep(0.5)

    time.sleep(3)
    pyautogui.hotkey("alt", "s")                       # Save case
    time.sleep(2)

    print("  EDI tab complete.")
    
def setup_case():
    """
    Create a new case for the first patient in Medisoft.
    Called from main.py as: case_setup.setup_case()
    """
    _open_new_case()
    _fill_personal_tab()
    print("  Personal tab complete.")

    _fill_account_tab()
    print("  Account tab complete.")

    _fill_diagnosis_tab()
    print("  Diagnosis tab complete.")

    _fill_policy_tab(1)
    _fill_policy_tab(2)
    _fill_policy_tab(3)
    print("  Policy tabs complete.")

    _fill_miscellaneous_tab()
    print("  Miscellaneous tab complete.")

    _fill_medicaid_tab()
    print("  Medicaid and Tricare tab complete.")

    _fill_comment_tab()
    print("  Comment tab complete.")

    _fill_edi_tab()
    print("  EDI tab complete.")
