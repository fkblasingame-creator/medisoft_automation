# main.py
from pages import application, practice_setup, provider_setup, user_setup, billing_setup, icd10_setup, insurance_setup, referring_provider_setup, address_setup, patient_setup

def build_new_practice():
    application.launch_medisoft()                       # Step 1
    practice_setup.create_new_practice()                # Step 2
    practice_setup.login()                              # Step 3
    practice_setup.fill_practice_info()                 # Step 4
    provider_setup.create_provider()                    # Step 5
    user_setup.create_users()                           # Step 6
    billing_setup.setup_billing_codes()                 # Step 7
    icd10_setup.setup_icd10_codes(count=3)              # Step 8
    insurance_setup.setup_insurance()                   # Step 9
    referring_provider_setup.setup_referring_provider() # Step 10
    address_setup.setup_attorney()                      # Step 11
    address_setup.setup_employer()                      # Step 12
    address_setup.setup_miscellaneous()                 # Step 13
    address_setup.setup_referral()                      # Step 14
    patient_setup.create_patient()                      # Step 15

if __name__ == "__main__":
    build_new_practice()