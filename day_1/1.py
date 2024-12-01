import pandas as pd

#TASK 1

#Importing the data and sorting the columns
df = pd.read_csv('1_data.txt', sep='\s+', header=None).apply(sorted)

total_distance = 0

#Iterating through the rows, adding the distances together
for row in df.itertuples():
  total_distance += abs(row[1] - row[2])

print(f'Total distance = {total_distance}')

#TASK 2

total_similarity = 0

#Iterating through the items in the first column, adding the 2nd_column_ferquency*item values together
for i in df[0]:
  total_similarity += i * sum((df[1] == i))

print(f'Total similarity = {total_similarity}')