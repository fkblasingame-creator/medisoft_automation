from pages import address_setup
import time

if __name__ == "__main__":
    address_setup.setup_attorney()
    time.sleep(2)
    address_setup.setup_employer()
    time.sleep(2)
    address_setup.setup_miscellaneous()
    time.sleep(2)
    address_setup.setup_referral()