import pandas as pd
import csv
import random
import copy
import os
#Firt-Feature

#Function to always have correct inputs
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

# load participant's data
formdata = pd.read_csv(participants_csv, sep=DELIMITER)
formdata = formdata.drop(["ID"], axis = 1)
Total_group = len(formdata)
print(Total_group)

#group size input = x
GS = read_integer("Please enter the group size: ")
n_groups = Total_group//GS
r_groups = Total_group%GS

i = 1
df_groups = {}

while len(formdata) > r_groups:
    homies = formdata.sample(n = GS)
    df_groups[f"group {i}"] = homies
    formdata = formdata.drop(index=homies.index)
    i += 1

if r_groups > 0:
    if r_groups < GS/2:
        
    else:
        i = +1
        df_groups[f"group {i}"] = formdata


print(f"\n{df_groups["group 1"]}")
print(f"\n{df_groups["group 2"]}")
print(f"\n{df_groups["group 3"]}")
#print(f"\n{df_groups["group 4"]}")
#print(f"\n{df_groups["group 5"]}")
print(f"\n{formdata}")
             
# print finishing message
print()
print("Job done.")