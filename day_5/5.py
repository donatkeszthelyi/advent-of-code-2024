import pandas as pd
import re

#TASK 1

#Reading the lines in the data
data = open("5_data.txt", 'r').readlines()

#Initializing the lists and the final result
rules = []
updates = []
correct_updates = []
result_1 = 0

#Regex for filtering the rules in the data
rule_regex = r"^\d+\|\d+$"

#Create the rules list and the updates list
for line in data:
    if re.match(rule_regex, line.strip()):
        rules.append(line.strip().split("|"))
    elif line.strip() != "":
        updates.append([int(x) for x in line.strip().split(",")])

#Dataframe from the rules list
rules_df = pd.DataFrame(rules, columns=["first", "second"]).astype(int)

#Finding the correct updates
for update in updates: #For every update
    is_correct = True
    for _, rule in rules_df.iterrows(): #For every rule
        if rule['first'] in update and rule['second'] in update: #If both number from the rule is in the update
            if update.index(rule['first']) > update.index(rule['second']): #Check whether the first number's index in the rule is lower than the second number's index
                is_correct = False
                break #If the update is incorrect, go to the next update
    if is_correct:
        correct_updates.append(update) #If the update is correct, append it to the correct updates list

for update in correct_updates:
    result_1 += update[len(update)//2] #Sum the middle numbers of the correct updates

print(f"Result 1 = {result_1}")

#TASK 2

#Creating the incorrect updates list
incorrect_updates = [update for update in updates if update not in correct_updates]

#Initializing the corrected updates list and the final result
corrected_updates = []
result_2 = 0

#Correcting the incorrect updates
for update in incorrect_updates: #For every incorrect update
    priority = {num: 0 for num in update} #Create a dictionary for the update, where each number in the update has an initial priority of 0
    for _, rule in rules_df.iterrows(): #For every rule
        if rule['first'] in update and rule['second'] in update: #If both number from the rule is in the update
            priority[rule['second']] += 1 #Increase the priority of the second number from the rule
  
    corrected_updates.append(sorted(update, key=lambda x: priority[x])) #Sort the update based on the priorities of the numbers

for update in corrected_updates:
    result_2 += update[len(update)//2] #Sum the middle numbers of the corrected updates

print(f"Result 2 = {result_2}")