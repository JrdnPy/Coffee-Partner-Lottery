import sys
import subprocess

# Function to check and install missing packages
def install(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Looks like you are missing the '{package}' library. Installing it now...")
        # This secretly runs "pip install [package]" in the background
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check and install our required packages
install('pandas')
install('gspread')

# Now it is safe to do your normal imports!
import pandas as pd
import gspread
import csv
import random
import copy
import os

#Function to always have correct integer inputs
def read_integer(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print("That was no valid number. Try again.")



# 1. Connect to Google Sheets
# Find the exact folder where this Python script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Stick the folder path and the filename together
cred_path = os.path.join(script_dir, 'credentials.json')

# Use that bulletproof path
gc = gspread.service_account(filename=cred_path)
spreadsheet = gc.open("API test UU")
worksheet = spreadsheet.worksheet("Answers to the form (1)")

# 2. Pull the data
data = worksheet.get_all_records()

# 3. Convert directly into a pandas DataFrame!
formdata = pd.DataFrame(data)