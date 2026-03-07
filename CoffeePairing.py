import pandas as pd
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

# path to the CSV files with participant data
participants_csv = "Coffee Partner Lottery participants.csv"

#Here you can choose what delimiter the csv uses
DELIMITER=','

# load participant's data from csv and clean if neccesary
formdata = pd.read_csv(participants_csv, sep=DELIMITER)
formdata = formdata.drop(["ID"], axis = 1)

#Greet the user and explain what this game is
print(f"""\n ====HOMIES MEET UP====
\nHi there, and welcome to homies meet up!
\nUsing this program random groups are generated of the currently signed up people. 
""")

#Show the current groupsize and ask how big you want the groups to be
Total_group = len(formdata)
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
if r_groups > 0:
    print(f"""\n there are {r_groups} people remaining how do you want to split them up? 
\n1. Randomly asign them to the full groups.
2. Create a new group of the remaining people. """)

    rem_split = read_integer("\nPlease make a choice: ")


if r_groups > 0: #If the reminder is bigger than 0 do this part else print the groups
    if rem_split == 1:
        while len(formdata) > 1: #check if the remaining people are more then one
            for key in dict_groups: #goes trough the groups in the dictionary and adds person to asign to one of the groups. does that until no one is remaing
                person_to_asign = formdata.sample(n=1)
                dict_groups[key] = pd.concat([dict_groups[key], person_to_asign])
                formdata = formdata.drop(index=person_to_asign.index)
    
    elif rem_split == 2: 
        dict_groups[f"group {i}"] = formdata

for group in dict_groups:
    groupx = dict_groups[group]
    print(f"\n===={group}====")
    print(f"{groupx}")
             
# print finishing message
print()
print("Job done.")