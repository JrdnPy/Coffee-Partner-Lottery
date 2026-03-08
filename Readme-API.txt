This Python program automatically reads a list of sign-ups from a Google Form/Sheet and randomly assigns participants into groups of a specified size. 

## 🛡️ Security Note for Grading
**To follow security best practices, the Google Cloud API credentials (`credentials.json`) have been intentionally excluded from this repository via `.gitignore`.** * **Team Members:** Please download the `credentials.json` file pinned in our group chat.
* **Professors/TAs:** If you need to run this code locally to test the API connection, please reach out to [Maksim Spirov/m.spirov@students.uu.nl] for the read-only credential file, or replace it with your own Google Service Account key.

## 🚀 Setup Instructions

1. **Clone the repository** to your local machine.
2. **Add the API Key:** Place the provided `credentials.json` file directly into the root folder of this project (in the exact same directory as `CoffeePairing.py`). Do not rename the file.
3. **Check your Python version:** Ensure you have Python 3.x installed. 

## 📦 Dependencies

You do not need to manually install any external libraries before running the script! The program includes an auto-installer that will check for and install the following required packages via `pip` if they are missing:
* `pandas` (for data manipulation)
* `gspread` (for Google Sheets API integration)

## 💻 How to Run

1. Open your terminal or command prompt.
2. Navigate to the project folder.
3. Run the script:
   ```bash
   python CoffeePairing.py