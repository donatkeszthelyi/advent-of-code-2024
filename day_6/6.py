import numpy as np

#TASK 1

#Read the data from the file and create the grid
data = open("6_data.txt", 'r').readlines()
grid = [list(line.strip()) for line in data]
array = np.array(grid)

#Locate the starting position of the guard
start = np.where((array == '^') | (array == '<') | (array == '>') | (array == 'v'))
x, y = start[0][0], start[1][0]

#Set to store visited locations
locations = set()
locations.add((x, y))

#Directions: up (0), right (1), down (2), left (3)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
current_direction = 0  # Start facing up

#Function to check if a move is valid
def is_valid_move(x, y):
    return (0 <= x < len(array) and 0 <= y < len(array[0]) and array[x, y] != '#')

#Function to check if a position is at the edge of the grid
def is_edge(x, y):
    return (x == 0 or x == len(array) - 1 or y == 0 or y == len(array[0]) - 1)

#Main loop for the guard's movement
while True:
    if is_edge(x, y):  #Check if at the edge
        break
    dx, dy = directions[current_direction]
    new_x, new_y = x + dx, y + dy

    if is_valid_move(new_x, new_y):
        x, y = new_x, new_y
        locations.add((x, y))  # ark the position as visited
    else:
        current_direction = (current_direction + 1) % 4  # Turn right
        dx, dy = directions[current_direction]
        if not is_valid_move(x + dx, y + dy):
            break  #Stop if no valid moves are possible

result_1 = len(locations)

print(f"Result 1 = {result_1}")