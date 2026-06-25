# pages/patient_setup.py
import pyautogui
import time
import random
from faker import Faker
from datetime import datetime

fake = Faker()

def create_patient():
    print("Navigating to Patient list...")
    pyautogui.hotkey('alt', 'l')
    time.sleep(3)
    pyautogui.press('p')
    time.sleep(3)
    
    print("Creating new patient...")
    pyautogui.hotkey('alt', 'n')
    time.sleep(6)
    
    print("Filling in main patient tab...")
    pyautogui.write(fake.last_name())
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.write(random.choice(['Jr', 'Sr', 'III', '']))  # Suffix
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.write(fake.first_name())
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.write(fake.first_name())  # Middle name
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.write(fake.street_address())
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.write(fake.secondary_address())  # Apartment
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.write(fake.zipcode())
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.write(fake.city())
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.write(fake.state_abbr())
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.press('tab')  # Skip back to Zip
    time.sleep(1)
    pyautogui.press('tab')  # Skip Country
    time.sleep(1)
    
    pyautogui.write(fake.email())  # Email - only once!
    pyautogui.press('tab')
    time.sleep(1.5)
    
    pyautogui.write(fake.msisdn()[:10])  # Home phone
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.write(fake.msisdn()[:10])  # Work phone
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.write(fake.msisdn()[:10])  # Cell phone
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.write(fake.msisdn()[:10])  # Fax
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.write(fake.msisdn()[:10])  # Other phone
    pyautogui.press('tab')
    time.sleep(1.5)
    
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90)
    pyautogui.write(dob.strftime("%m/%d/%Y"))
    pyautogui.press('tab')
    time.sleep(1.5)
    
    pyautogui.write(random.choice(['m', 'f']))  # Sex
    pyautogui.press('tab')
    time.sleep(1.5)
    
    pyautogui.write(str(random.randint(1, 99)))  # Birth weight
    pyautogui.press('tab')
    time.sleep(1.5)
    
    pyautogui.write(random.choice(['p', 'g']))  # Weight unit
    pyautogui.press('tab')
    time.sleep(1.5)
    
    pyautogui.write(str(random.randint(100000000, 999999999)))  # SSN
    pyautogui.press('tab')
    time.sleep(1.5)
    
    pyautogui.write('p')  # Entity type - Person
    pyautogui.press('tab')
    time.sleep(1.5)
    
    pyautogui.write(random.choice(['h', 'd']))  # Ethnicity
    pyautogui.press('tab')
    time.sleep(1.5)
    
    pyautogui.write('e')  # Language - English
    pyautogui.press('tab')
    time.sleep(1.5)
    
    # Skip Death Date with tab
    pyautogui.press('tab')
    time.sleep(1.5)
    
    # Race checkboxes - skip with tab
    pyautogui.press('tab')
    time.sleep(1.5)
    
    pyautogui.write(random.choice(['f', 'm', 'u']))  # Birth Sex
    pyautogui.press('tab')
    time.sleep(1.5)
    
    pyautogui.write(random.choice(['l', 's', 'u']))  # Sexual Orientation
    pyautogui.press('tab')
    time.sleep(1.5)
    
    pyautogui.write(random.choice(['s', 'b', 'd']))  # Gender Identity
    pyautogui.press('tab')
    time.sleep(1.5)
    
    pyautogui.write(random.choice(['c', 'f', 'm']))  # Marital Status
    pyautogui.press('tab')
    time.sleep(3)
    
    print("Navigating to Other Information tab...")
    pyautogui.hotkey('alt', 'o')
    pyautogui.press('tab')
    time.sleep(2)
    
    pyautogui.press('tab')  # Assigned provider
    time.sleep(2)
    
    pyautogui.write(fake.last_name())  # Patient ID 2
    pyautogui.press('tab')
    time.sleep(2)
    
    pyautogui.press('tab')
    time.sleep(2)
    
    pyautogui.write('Code')  # Patient indicator
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.press('tab')  # Flag
    time.sleep(1)
    
    pyautogui.write('ID')  # Healthcare ID
    pyautogui.press('tab')
    time.sleep(1)
    
    pyautogui.press('space')  # Signature on file
    pyautogui.press('tab')
    time.sleep(2)
    
    # Signature date - past date only
    pyautogui.write(fake.date_between(start_date='-5y', end_date='today').strftime('%m/%d/%Y'))
    pyautogui.press('tab')
    time.sleep(2)
    
    pyautogui.press('tab', presses=6)
    time.sleep(1.5)
    
    pyautogui.write(fake.first_name())  # Emergency contact
    pyautogui.press('tab')
    time.sleep(2)
    
    pyautogui.write(fake.msisdn()[:10])  # Emergency home phone
    pyautogui.press('tab')
    time.sleep(2)
    
    pyautogui.write(fake.msisdn()[:10])  # Emergency cell phone
    pyautogui.press('tab')
    time.sleep(2)
    
    pyautogui.press('tab', presses=6)
    time.sleep(2)
    
    pyautogui.press('space')  # Web enabled
    pyautogui.press('tab')
    time.sleep(2)
    
    pyautogui.write('10')
    time.sleep(1)
    
    print("Saving patient...")
    pyautogui.hotkey('alt', 's')
    time.sleep(2)
    print("Patient created!")

if __name__ == "__main__":
    create_patient()