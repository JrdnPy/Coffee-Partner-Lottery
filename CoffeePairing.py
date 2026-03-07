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
df_groups = {}

while len(formdata) > r_groups:
    homies = formdata.sample(n = GS)
    df_groups[f"group {i}"] = homies
    formdata = formdata.drop(index=homies.index)
    i += 1

#Ask how you want the remainders to be split up and split them up if there are people remaining.
if r_groups > 0:
    print(f"""\n there are {r_groups} people remaining how do you want to split them up? 
    \n1. Randomly asign them to the full groups.
2. Create a new group of the remaining people. """)

    rem_split = read_integer("\nPlease make a choice: ")

'''
if r_groups > 0:
    if r_groups < GS/2:
        
    else:
        i = +1
        df_groups[f"group {i}"] = formdata
'''

print(f"\n{df_groups["group 1"]}")
print(f"\n{df_groups["group 2"]}")
print(f"\n{df_groups["group 3"]}")
#print(f"\n{df_groups["group 4"]}")
#print(f"\n{df_groups["group 5"]}")
print(f"\n{formdata}")
             
# print finishing message
print()
print("Job done.")