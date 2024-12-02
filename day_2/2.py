import pandas as pd

#TASK 1

#Importing the data
df = pd.read_csv('2_data.txt', sep='\s+', header=None)

#Defining the logic for the adjacent difference check
def adj_diff_check(row):
    
    row = row.dropna() #Drop NaN values
  
    #Check if any adjacent pair has a difference between 1 and 3 (inclusive)
    for i in range(len(row) - 1):
        if not (1 <= abs(row.iloc[i] - row.iloc[i + 1]) <= 3):
            return False
    return True

#Defining the logic for the strict monotonity check
def strict_monotonity_check(row):

    row = row.dropna() #Drop NaN values

    #Check if strictly increasing
    increasing = list(row) == sorted(row)
    #Check if strictly decreasing
    decreasing = list(row) == sorted(row, reverse=True)
    
    return increasing or decreasing

#Filtering through the dataframe, checking if a row is strictly increasing or strictly decreasing, and has an adjacent pair with a difference between 1 and 3
safe_count_1 = len(df[df.apply(lambda row: 
                              strict_monotonity_check(row) and 
                              adj_diff_check(row), axis=1)])

print(f"Safe count 1 = {safe_count_1}")

#TASK 2

#Defining the logic for the checks after value dropping
def check_with_one_dropped(row):
    
    row = row.dropna() #Drop NaN values

    for i in range(len(row)):
        row_without_i = row.drop(index=row.index[i]) #Drop the i-th value

        #Check if the row without the i-th value satisfies both conditions
        if strict_monotonity_check(row_without_i) and adj_diff_check(row_without_i):
            return True
        
    return False

#Filtering through the dataframe, checking every row with the check_with_one_dropped function
safe_count_2 = len(df[df.apply(lambda row: check_with_one_dropped(row), axis=1)])

print(f"Safe count 2 = {safe_count_2}")