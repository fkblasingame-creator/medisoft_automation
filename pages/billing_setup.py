# pages/billing_setup.py
import pyautogui
import time
import csv
import random
import os

def get_random_cpt():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'CPT_clean.csv')
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return random.choice(rows)

def create_cpt_code():
    print("Navigating to Procedure/Payment/Adjustment codes...")
    pyautogui.hotkey('alt', 'l')
    time.sleep(2)
    pyautogui.press('j')
    time.sleep(2)

    print("Creating new CPT code...")
    pyautogui.hotkey('alt', 'n')
    time.sleep(2)

    cpt = get_random_cpt()
    print(f"Using CPT code: {cpt['Code']} - {cpt['Description']}")

    pyautogui.write(cpt['Code'])
    pyautogui.press('tab')
    time.sleep(0.5)

    # ImportCPT handled description in original - do it here
    pyautogui.write(cpt['Description'])
    pyautogui.press('tab')  # Skip to after description
    time.sleep(0.5)

    pyautogui.press('tab')  # Skip Code Type
    time.sleep(0.5)

    pyautogui.write('a')  # Account code
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('1')  # Type of service
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('10')  # POS
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('5')  # Time to do procedure
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('a')  # Service classification
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('Aetna')  # Don't bill
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('Cigna')  # Only bill
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('MM')  # Mod 1
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('MM')  # Mod 2
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('Mb')  # Mod 3
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('MM')  # Mod 4
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.press('tab')  # Skip Revenue code
    time.sleep(0.5)

    pyautogui.write('2')  # Default units
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('3')  # NDC
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('10')  # NDC unit price
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('G')  # NDC measurement
    pyautogui.press('tab')
    time.sleep(2)

    pyautogui.write('a')  # Code ID qualifier
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('100')  # PSA
    pyautogui.press('tab')
    time.sleep(2)

    pyautogui.write(cpt['CPTDescription'])
    time.sleep(1)

    pyautogui.hotkey('alt', 'a')
    time.sleep(1)
    pyautogui.write('1200')
    pyautogui.hotkey('alt', 's')
    time.sleep(1)
    print(f"CPT code {cpt['Code']} saved!")

def create_adjustment_code():
    print("Creating adjustment code...")
    pyautogui.hotkey('alt', 'n')
    time.sleep(1)

    pyautogui.write('ADJ')
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('Adjustment')
    pyautogui.press('tab')
    time.sleep(2)

    pyautogui.write('a')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('2')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('adj')  # Alt code 2
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.write('adj')  # Alt code 3
    time.sleep(3)

    pyautogui.hotkey('alt', 'a')
    time.sleep(1)
    pyautogui.write('0')
    pyautogui.hotkey('alt', 's')
    time.sleep(1)
    print("Adjustment code saved!")

def create_cash_payment():
    print("Creating cash payment code...")
    pyautogui.hotkey('alt', 'n')
    time.sleep(3)

    pyautogui.write('Cash')
    pyautogui.press('tab')
    time.sleep(1)

    pyautogui.write('cash')
    pyautogui.press('tab')
    time.sleep(2)

    for _ in range(12):
        pyautogui.press('down')
        time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(1)

    pyautogui.write('a')
    pyautogui.press('tab')
    time.sleep(1)

    pyautogui.write('2')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(3)

    pyautogui.hotkey('alt', 's')
    time.sleep(3)
    print("Cash payment code saved!")

def create_simple_codes():
    print("Creating simple payment/adjustment codes...")

    # These codes only need: code, description, alt description
    codes = [
        ('INSPAY',    'Insurance Payment',            'INSUrance payment'),
        ('TakeBack',  'Insurance Takeback Adjustment', 'INSUrance takeback'),
        ('Withhold',  'Insurance Withhold Adjustment', 'INSUrance withhold'),
        ('COMMENT',   'Comment',                       'COMMENT'),
        ('CashCoPay', 'Cash Copayment',                'CASH copay'),
        ('CheckCoPay','Check Copayment',               'CHECK copay'),
        ('CCCOPay',   'Credit Card Copayment',         'CREDIT CARD copay'),
        ('CheckPay',  'Check Payment',                 'CHECK payment'),
        ('CCPAY',     'Credit Card Payment',           'CREDIT CARD payment'),
        ('DED',       'Deductible',                    'DEDUCTIBLE'),
    ]

    for code_id, desc, alt_desc in codes:
        print(f"Creating code: {code_id}")
        pyautogui.hotkey('alt', 'n')
        time.sleep(3)

        pyautogui.write(code_id)
        pyautogui.press('tab')
        time.sleep(1)

        pyautogui.write(desc)
        pyautogui.press('tab')
        time.sleep(2)

        pyautogui.write(alt_desc)
        pyautogui.press('tab')
        time.sleep(3)

        pyautogui.hotkey('alt', 's')
        time.sleep(2)
        print(f"Code {code_id} saved!")

def setup_billing_codes():
    create_cpt_code()
    create_adjustment_code()
    create_cash_payment()
    create_simple_codes()

    print("Editing first code...")
    pyautogui.hotkey('alt', 'i')
    time.sleep(3)
    pyautogui.hotkey('alt', 'a')
    time.sleep(1)
    pyautogui.write('500')
    pyautogui.hotkey('alt', 's')
    time.sleep(2)

    print("Closing billing codes...")
    pyautogui.hotkey('alt', 'c')
    pyautogui.press('enter')
    print("All billing codes created!")

if __name__ == "__main__":
    setup_billing_codes()