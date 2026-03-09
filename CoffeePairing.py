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

import pandas as pd
import gspread
import os

#Function to always have correct integer inputs
def read_integer(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print("That was no valid number. Try again.")


# connection to Google Sheets
script_dir = os.path.dirname(os.path.abspath(__file__))

#folder path and the filename 
cred_path = os.path.join(script_dir, 'credentials.json')

#pathing
gc = gspread.service_account(filename=cred_path)
spreadsheet = gc.open("API test UU")
worksheet = spreadsheet.worksheet("Answers to the form (1)")

# 2. Pull the data
data = worksheet.get_all_records()

#Conversion of data into dataframe and cleaning
formdata = pd.DataFrame(data)
formdata = formdata.drop(["Time"], axis = 1)
formdata.columns = ["Name:", "Email:"]

# path to the CSV files with conversation starters data
conversation_csv = "Conversation_starters.csv"

#load conversation starters
conversation_starters = pd.read_csv(conversation_csv, sep = '\t')

print("""
      
Welcome to "Get to know a local Homie".
      
Before we initiate group size selection and creation we must explain how this programme works.
      
      
      """)
      
      
input("""
      
      'Enter' to continue
      
      """)
    
print("""
      
1. Participants should sign up by filling in their Name and Email in the
   the google form that can be found inside our "Documentation" document located within the ZIP folder.

2. This program automatically reads the survey responses, therefore there is
   no need to manually download any CSV file.
 
3. You can add or change participants at any time between rounds.

4. For testing or grading, you can also directly edit the responses in the survey,
   through the google sheets or the form itself (links found in "documentation")
   
5. After adding participants, simply run the program again to generate new groups.

The program will now load the current list of participants.
      
      """)


input("""
      
      'Enter' to continue
      
      """)


#Greet the user and explain what this game is
print(f"""\n ====HOMIES MEET UP====
\nHi there, and welcome to homies meet up!
\nUsing this program random groups are generated of the currently signed up people. 
""")

#Show the current groupsize and ask how big you want the groups to be
Total_group = len(formdata)

if Total_group == 1:
    print("""
          
          This is an insufficient amount of participants.
          
          Please find some friends :(
          
          The programme will now terminate.
          
          """)
    sys.exit(0)
    
if Total_group == 0:
    print("""
          
          This is an insufficient amount of participants.
          
          Please find some friends :(
          
          The programme will now terminate.
          
          """)
    sys.exit(0)

print(f"""\nThe total amount of signed up people are: {Total_group}""")
GS = read_integer("Please enter how large you want each group to be: ")

while True:
    if GS > Total_group/2:
        GS = read_integer(f"\nGroups size cannot be larger that half the groupsize ({Total_group/2}) please try again: ")
    elif GS < 2: 
        GS = read_integer(f"\nGroups size cannot be smaller then 2 please try again: ")
    else:
        break
    
#Calculate the amount of groups and the remainder
n_groups = Total_group//GS
r_groups = Total_group%GS

#Spilt the people up in random groups which are stored in dataframes. the dataframes are stored in a dictionary. 
i = 1
dict_groups = {}

while len(formdata) > r_groups: # Makes the code run until you cannot create full groups. 
    homies = formdata.sample(n = GS) # Homies will be a the newly formed group the sample function randomly pics x amount out of a dataframe. 
    dict_groups[f"Group {i}"] = homies # Store the current Homies as group x inside of a dictionary with the key being group x
    formdata = formdata.drop(index=homies.index) #  remove the current homies from the total list. 
    i += 1 # increase group by 1

#Ask how you want the remainders to be split up and split them up if there are people remaining.
if r_groups > 1:
    print(f"""\n there are {r_groups} people remaining how do you want to split them up? 
\n1. Randomly asign them to the full groups.
2. Create a new group of the remaining people. """)
    rem_split = read_integer("\nPlease make a choice: ")

elif r_groups == 1: #If there is only 1 person reandomy asign them to one of the groups
    print("\nYou cannot have a group of one person, so the remaining person will be randomly assigned to one of the groups.")
    input("\nPress enter to continue...")
    rem_split = 1




if r_groups > 0: #If the reminder is bigger than 0 do this part else print the groups
    if rem_split == 1:
        while len(formdata) > 0: #check if the remaining people are more then one
            for key in list(dict_groups.keys()):#goes trough the groups in the dictionary and adds person to asign to one of the groups. does that until no one is remaing
                if len(formdata) == 0:
                    break                 
                person_to_asign = formdata.sample(n=1)
                dict_groups[key] = pd.concat([dict_groups[key], person_to_asign])
                formdata = formdata.drop(index=person_to_asign.index)
    
    elif rem_split == 2: 
        dict_groups[f"Group {i}"] = formdata #since we are removing from the total list the remainders here will become the last group
        

#Create a clean output of the groups with the starters. 
for Group in dict_groups:
    Groupx = dict_groups[Group]
    print(f"\n\n========== {Group} ==========")
    print("\nThese people are your Homies this week!!")
    print(f"\n{Groupx}")
    print(f"""\nSo you have an easier time starting the conversation, here is a starter:
\n{conversation_starters.iloc[:,0].sample(n=1).iloc[0]}""")
             
# print finishing message
print("\nJob done.\n")