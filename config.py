# config.py - All settings and practice data
from faker import Faker

fake = Faker()

# Medisoft path
MEDISOFT_PATH = r'C:\Medisoft\BIN\mapa.exe'

# Asset image paths
LOGIN_SCREEN = r'assets/login_screen.png'
OPEN_PRACTICE = r'assets/open_practice.png'
CREATE_PRACTICE_DIALOG = r'assets/create_practice_dialog.png'

# Login credentials
USERNAME = 'SYSTEM'
PASSWORD = 'MEDISOFT1'

# Practice data
PRACTICE_NAME = fake.company()
FOLDER_NAME = fake.word().upper()
STREET_ADDRESS = fake.street_address()
CITY = fake.city()
STATE = fake.state_abbr()
ZIP = fake.zipcode()
PHONE = fake.numerify('##########')
EXTENSION = fake.numerify('###')
ALT_PHONE = fake.numerify('##########')
FAX = fake.numerify('##########')
EMAIL = fake.email()
INITIAL = fake.random_letter().lower()
FEDERAL_TAX_ID = fake.numerify('##-#######')
NPI_NUMBER = fake.numerify('##########')
EXTRA1 = fake.word()[:30]
EXTRA2 = fake.word()[:30]

# Provider data
PROVIDER_LAST_NAME = fake.last_name()
PROVIDER_FIRST_NAME = fake.first_name()
PROVIDER_MIDDLE_NAME = fake.first_name()
PROVIDER_CREDENTIALS = fake.random_element(elements=['MD', 'DO', 'RN', 'NP', 'PA'])
PROVIDER_STREET = fake.street_address()
PROVIDER_ZIP = fake.zipcode()
PROVIDER_CITY = fake.city()
PROVIDER_STATE = fake.state_abbr()
PROVIDER_EMAIL = fake.email()
PROVIDER_OFFICE_PHONE = fake.numerify('##########')
PROVIDER_FAX = fake.numerify('##########')
PROVIDER_HOME_PHONE = fake.numerify('##########')
PROVIDER_CELL_PHONE = fake.numerify('##########')
PROVIDER_LICENSE = fake.bothify(text='???####')