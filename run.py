import gspread
from google.oauth2.service_account import Credentials

# Define the scopes for Google Sheets API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from the creds.json file
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the Google Sheet by its name
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# Select a worksheet by index (0 refers to the first sheet)
worksheet = SHEET.get_worksheet(0)

# Fetch some data from the first row to test the connection
test_data = worksheet.row_values(3)

# Print the fetched data to confirm the connection
print("Connected to Google Sheet successfully. Here's the data from the first row:")
print(test_data)