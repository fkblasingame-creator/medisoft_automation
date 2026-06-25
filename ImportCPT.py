import csv
import random
import pyautogui
import time

def get_random_cpt():
    with open("CPT_clean.csv", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return random.choice(rows)

# Give yourself time to click into the CPT Code field
print("Click into the CPT Code field... typing starts in 3 seconds")
time.sleep(1)

cpt = get_random_cpt()

# Type the CPT code
pyautogui.write(cpt["Code"])

# Press TAB
pyautogui.press("tab")

# Type the description
pyautogui.write(cpt["Description"])
