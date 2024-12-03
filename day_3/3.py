import pandas as pd
import re

#TASK 1

#Reading the data
data = open("3_data.txt", "r").read()

#Regex for the correct mul formulas
regex = r"mul\(\d{1,3},\d{1,3}\)"

#Finding all the correct mul formulas and parsing them
muls = re.findall(regex, data, re.MULTILINE)
parsed_muls = [re.findall(r"\d{1,3}", match) for match in muls]

#Creating a dataframe with the numbers as integers
df = pd.DataFrame(parsed_muls, columns=["first", "second"]).astype(int)

#Multiplying each line and getting the sum of the results
result_1 = (df.prod(axis=1)).sum()

print(f"Answer 1 = {result_1}")

#TASK 2

#Setting initial enabled condition to true
enabled = True

#Initialising the result variable
result_2 = 0

#Regex for finding either correct mul formulas or don't() or do() instructions (note: I use regex capturing groups for the numbers)
regex_2 = r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)"

#Iterating through matches that satisfy the regex
for match in re.finditer(regex_2, data):
    if match.group(0) == "don't()": #If the whole match (group(0) is the whole string in the match) is don't(), set enabled to false
        enabled = False
    elif match.group(0) == "do()": #Set enabled to true
        enabled = True
    elif match.group(0).startswith("mul"):
        if enabled: #Only process mul instructions if they are enabled
            first = int(match.group(1)) #Assign the first regex capturing group to the first number in the match
            second = int(match.group(2)) #Assign the second regex capturing group to the second number in the match
            result_2 += first * second #Adding the product to the end result

print(f"Answer 2 = {result_2}")
