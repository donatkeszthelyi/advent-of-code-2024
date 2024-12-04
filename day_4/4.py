import pandas as pd

#TASK 1

#Load data into a DataFrame
lines = []
with open("4_data.txt", 'r') as file:
    for line in file:
        lines.append(line.strip())
df = pd.DataFrame([list(line) for line in lines])

#Initializing counters for occurrences in different orientations
total_xmas_horizontal_lr = 0  #Left-to-right
total_xmas_horizontal_rl = 0  #Right-to-left
total_xmas_vertical_tb = 0    #Top-to-bottom
total_xmas_vertical_bt = 0    #Bottom-to-top
total_xmas_diagonal = 0       #Diagonal

#Counting horizontally
for row in df.itertuples(index=False):
    row_values = list(row)
    #Left-to-right
    for i in range(len(row_values) - 3):
        if row_values[i:i+4] == ['X', 'M', 'A', 'S']:
            total_xmas_horizontal_lr += 1
    #Right-to-left
    for i in range(len(row_values) - 3):
        if row_values[i:i+4] == ['S', 'A', 'M', 'X']:
            total_xmas_horizontal_rl += 1

#Counting vertically
df_transposed = df.T
for col in df_transposed.itertuples(index=False):
    col_values = list(col)
    #Top-to-bottom
    for i in range(len(col_values) - 3):
        if col_values[i:i+4] == ['X', 'M', 'A', 'S']:
            total_xmas_vertical_tb += 1
    #Bottom-to-top
    for i in range(len(col_values) - 3):
        if col_values[i:i+4] == ['S', 'A', 'M', 'X']:
            total_xmas_vertical_bt += 1

#Function to extract diagonals
def get_all_diagonals(matrix):
    diagonals = []
    rows, cols = len(matrix), len(matrix[0])
    #Top-left to bottom-right diagonals
    for d in range(-(rows - 1), cols):
        diagonal_tl_br = [matrix[i][i - d] for i in range(max(0, d), min(rows, cols + d))]
        diagonals.append(diagonal_tl_br)
    #Top-right to bottom-left diagonals
    for d in range(-(rows - 1), cols):
        diagonal_tr_bl = [matrix[i][cols - 1 - (i - d)] for i in range(max(0, d), min(rows, cols + d))]
        diagonals.append(diagonal_tr_bl)
    return diagonals

#Converting dataframe to a list of lists
matrix = df.values.tolist()

#Extracting all diagonals
diagonals = get_all_diagonals(matrix)

#Counting diagonally
for diagonal in diagonals:
    for i in range(len(diagonal) - 3):
        if diagonal[i:i+4] == ['X', 'M', 'A', 'S'] or diagonal[i:i+4] == ['S', 'A', 'M', 'X']:
            total_xmas_diagonal += 1

total_1 = total_xmas_horizontal_lr + total_xmas_horizontal_rl + total_xmas_vertical_tb + total_xmas_vertical_bt + total_xmas_diagonal

print(f"Total XMAS-s = {total_1}")

#TASK 2

total_2 = 0

for i in range(df.shape[0]-2): #For every row (except the last 2) in the database
  for v in range(df.iloc[i].shape[0]-2): #For every value (except the last 2) in the row
    #Incrementing the count if one of the 4 conditions apply (one for every X-MAS layout)
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