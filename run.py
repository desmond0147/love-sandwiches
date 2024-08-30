import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    """Get sales figures input from user and validate them."""
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10, 20, 30, 40, 50, 60\n")

        # Collect data from user input
        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")

        # Validate the collected sales data
        if validate_data(sales_data):
            # Convert to integer list after validation
            sales_data = [int(value) for value in sales_data]
            print("Data is valid:", sales_data)
            return sales_data  # Return the validated sales data

def validate_data(values):
    """
    Converts all string values into integers.
    Raises ValueError if strings cannot be converted into integers or if there aren't exactly 6 values.
    Returns True if data is valid, otherwise False.
    """
    try:
        # Check if the number of values is exactly 6
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values required, you provided {len(values)}")

        # Attempt to convert each value to an integer to ensure they are valid numbers
        [int(value) for value in values]

        # If everything passes, return True
        return True

    except ValueError as e:
        # Catch the ValueError and print the error message
        print(f"Invalid data: {e}, please try again.\n")
        return False



def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into worksheet update,
    the relevant worksheet with data provided. 
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as sales figure subtracted from stock:
    - Positive surplus indicates waste.
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()  
    stock_row =stock[-1]
     
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)

    return surplus_data


def main():
    """
    Run all program functions.
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]  # Get sales data from user input
    update_worksheet(sales_data, "sales")  # Update the sales worksheet
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")

print("Welcome to Love Sandwiches Automation")
main()

