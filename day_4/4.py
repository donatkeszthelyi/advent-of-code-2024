import numpy as np
import pandas as pd

#TASK 1

#Load data into a DataFrame
lines = []
with open("4_data.txt", 'r') as file:
    for line in file:
        lines.append(line.strip())
df = pd.DataFrame([list(line) for line in lines])

#Initializing counters
xmas_horizontal = 0
xmas_vertical = 0
xmas_diagonal = 0

#Counting horizontally
for row in df.itertuples(index=False):
    row_values = list(row)
    for i in range(len(row_values) - 3):
        if row_values[i:i+4] == ['X', 'M', 'A', 'S'] or row_values[i:i+4] == ['S', 'A', 'M', 'X']:
            xmas_horizontal += 1

#Counting vertically
df_transposed = df.T
for col in df_transposed.itertuples(index=False):
    col_values = list(col)
    for i in range(len(col_values) - 3):
        if col_values[i:i+4] == ['X', 'M', 'A', 'S'] or col_values[i:i+4] == ['S', 'A', 'M', 'X']:
            xmas_vertical += 1

#Function to extract diagonals
def get_all_diagonals(matrix):
    diagonals = []
    np_matrix = np.array(matrix)
    rows, cols = np_matrix.shape
    #Top-left to bottom-right diagonals
    for d in range(-(rows - 1), cols):
        diagonal_tl_br = np_matrix.diagonal(offset=d)
        diagonals.append(list(diagonal_tl_br))
    #Top-right to bottom-left diagonals
    flipped_matrix = np.fliplr(np_matrix)  #Flip the matrix horizontally
    for d in range(-(rows - 1), cols):
        diagonal_tr_bl = flipped_matrix.diagonal(offset=d)
        diagonals.append(list(diagonal_tr_bl))

    return diagonals

#Converting dataframe to a list of lists
matrix = df.values.tolist()

#Extracting all diagonals
diagonals = get_all_diagonals(matrix)

#Counting diagonally
for diagonal in diagonals:
    for i in range(len(diagonal) - 3):
        if diagonal[i:i+4] == ['X', 'M', 'A', 'S'] or diagonal[i:i+4] == ['S', 'A', 'M', 'X']:
            xmas_diagonal += 1

total_1 = xmas_horizontal + xmas_vertical + xmas_diagonal

print(f"Total XMAS-s = {total_1}")

#TASK 2

total_2 = 0

for i in range(df.shape[0]-2): #For every row (except the last 2) in the database
  for v in range(df.iloc[i].shape[0]-2): #For every value (except the last 2) in the row
    #Incrementing the count if one of the 4 conditions applies (one for every X-MAS layout)
    if df.iloc[i][v] == 'M' and df.iloc[i][v+2] == 'M': #First possible layout
        if df.iloc[i+1][v+1] == 'A':
          if df.iloc[i+2][v] == 'S' and df.iloc[i+2][v+2] == 'S':
              total_2 += 1
    if df.iloc[i][v] == 'M' and df.iloc[i][v+2] == 'S': #Second possible layout
        if df.iloc[i+1][v+1] == 'A':
          if df.iloc[i+2][v] == 'M' and df.iloc[i+2][v+2] == 'S':
              total_2 += 1
    if df.iloc[i][v] == 'S' and df.iloc[i][v+2] == 'M': #Third possible layout
        if df.iloc[i+1][v+1] == 'A':
          if df.iloc[i+2][v] == 'S' and df.iloc[i+2][v+2] == 'M':
              total_2 += 1
    if df.iloc[i][v] == 'S' and df.iloc[i][v+2] == 'S': #Fourth possible layout
        if df.iloc[i+1][v+1] == 'A':
          if df.iloc[i+2][v] == 'M' and df.iloc[i+2][v+2] == 'M':
              total_2 += 1

print(f"Total X-MAS-s = {total_2}")