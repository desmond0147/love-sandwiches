import gspread
from google.oauth2.service_account import Credentials

# Define the scopes required for the Google Sheets and Drive APIs
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from the creds.json file
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """Get sales figures input from user."""
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10, 20, 30, 40, 50, 60\n")

    # Collect data from user input
    data_str = input("Enter your data here: ")
    sales_data = data_str.split(",")

    # Validate the collected sales data
    validate_data(sales_data)

def validate_data(values):
    """
    Converts all string values into integers.
    Raises ValueError if strings cannot be converted into integers or if there aren't exactly 6 values.
    """
    try:
        # Check if the number of values is exactly 6
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values required, you provided {len(values)}")
        
        # Convert the values to integers
        int_values = [int(value) for value in values]
        print("Data is valid:", int_values)
        
    except ValueError as e:
        # Catch the ValueError and print the error message
        print(f"Invalid data: {e}")

# Run the function to test
get_sales_data()