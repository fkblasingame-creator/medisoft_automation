# Medisoft Practice Automation

A Python-based desktop automation suite for building and populating CGM Medisoft medical practice management software with test data. Built using PyAutoGUI and the Faker library, this project automates the complete setup of a new medical practice — from initial configuration through full patient case creation across all tabs.

## What It Does

Automates the complete Medisoft practice setup workflow:

1. Launch Medisoft and create a new practice
2. Configure practice information
3. Create providers, users, and billing codes
4. Generate ICD-10 diagnosis codes
5. Set up insurance carriers
6. Add referring providers
7. Create all address types (Attorney, Employer, Miscellaneous, Referral Source)
8. Create patients
9. Build complete patient cases including:
   - Personal tab (employer, employment info)
   - Account tab (assigned, referring, supervising providers, referral source, attorney, facility)
   - Diagnosis tab (4 diagnosis codes)
   - Policy 1, 2, and 3 tabs (insurance carriers, policy numbers, group info)
   - Miscellaneous tab
   - Medicaid and Tricare tab
   - Comment tab
   - EDI tab

## Tech Stack

- **Python 3.x**
- **PyAutoGUI** — keyboard and mouse automation
- **Faker** — realistic fake data generation
- **icd10** — ICD-10 code lookup and validation

## Project Structure

```
medisoft_automation/
├── main.py                          # Full end-to-end practice setup
├── config.py                        # Global settings and constants
├── requirements.txt
├── automation.log                   # Runtime log (auto-generated)
├── assets/                          # Reference screenshots
│   ├── create_practice_dialog.png
│   ├── login_screen.png
│   └── open_practice.png
├── data/
│   └── CPT_clean.csv                # CPT billing codes
├── pages/                           # Modular page automation scripts
│   ├── __init__.py
│   ├── application.py               # Launch and initialize Medisoft
│   ├── practice_setup.py            # Practice creation and login
│   ├── provider_setup.py            # Provider creation (standalone + F8)
│   ├── user_setup.py                # User and security setup
│   ├── billing_setup.py             # CPT billing codes
│   ├── icd10_setup.py               # ICD-10 diagnosis codes
│   ├── insurance_setup.py           # Insurance carrier setup
│   ├── referring_provider_setup.py  # Referring provider (standalone + F8)
│   ├── address_setup.py             # Attorney, employer, misc, referral (standalone + F8)
│   ├── facility_setup.py            # Facility setup (standalone + F8)
│   ├── patient_setup.py             # Patient demographics
│   └── case_setup.py                # Full patient case with all 12 tabs
└── tests/                           # Individual module test scripts
    ├── test_icd10.py
    ├── test_insurance.py
    ├── test_user_setup.py
    ├── test_address.py
    ├── test_referring_provider.py
    ├── test_facility.py
    ├── test_case.py
    ├── test_diagnosis.py
    ├── test_policy.py
    ├── test_misc.py
    ├── test_comment.py
    └── test_edi.py
```

## Design Pattern

This project follows the **Page Object Model** pattern — the same architecture used in professional Selenium and Playwright test suites. Each module in `pages/` represents a distinct screen or workflow in Medisoft, with:

- A public entry function (e.g., `setup_insurance()`) called by `main.py`
- Private helper functions (prefixed with `_`) for internal navigation and field filling
- F8 variants of key functions (e.g., `_fill_provider_f8()`) for use when forms are opened inline from within other dialogs
- Shared utilities reused across modules (address, provider, facility creation)

## Key Engineering Decisions

- **F8 form variants**: Many Medisoft dialogs can be opened inline via F8 from within other forms. Each reusable module has both a standalone version (navigates via the Lists menu) and an F8 version (cursor already positioned, no navigation needed).
- **Modular tab functions**: The patient case is broken into one function per tab, making it easy to test, debug, and extend individual sections without running the full workflow.
- **Centralized fake data**: All test data is generated using the Faker library — no real PHI is ever used or stored.
- **Timing tuned for reliability**: Sleep intervals are calibrated to allow Medisoft's UI to respond between actions, with longer waits after dialog opens and saves.

## Getting Started

### Prerequisites

- Windows OS (Medisoft is Windows-only)
- Medisoft installed and licensed
- Python 3.x installed

### Installation

```bash
git clone https://github.com/fkblasingame-creator/medisoft_automation
cd medisoft-automation
pip install -r requirements.txt
```

### Running the Full Setup

Open Medisoft to the starting screen, then run:

```bash
python main.py
```

### Running Individual Modules

Each module can be tested independently:

```bash
python tests/test_insurance.py
python tests/test_icd10.py
python tests/test_case.py
```

### Resuming After a Failure

If `main.py` fails mid-run, comment out the completed steps and re-run from the failure point:

```python
def build_new_practice():
    # application.launch_medisoft()        # Step 1  ✅
    # practice_setup.create_new_practice() # Step 2  ✅
    # ...
    case_setup.setup_case()               # Step 15 ← resume here
```

## Important Notes

- All patient and practice data generated by this tool is **entirely fake** using the Faker library
- No real PHI (Protected Health Information) is used or stored
- This tool is intended for **testing and training environments only**
- Timing delays may need adjustment for different hardware or network speeds

## Author

Built and maintained as a portfolio project demonstrating Python automation, modular code design, and real-world application of the Page Object Model pattern in a healthcare software context.