# Libraries
import timeit

# Read Input Data
def read_txt(txt_file):
    f = open(txt_file, "r")
    return f.read().splitlines()

day11_input = read_txt("day11/day11_input.txt")

# numero = 1
# new_input = []

# for line in day11_input:
#     new_line = ''
#     for char in line:
#         if char == '#':
#             new_line += str(numero)
#             numero += 1
#         else:
#             new_line += char
#     new_input.append(new_line)



# Create dictionary
dict_test = dict()
numero = 0

for i in range(len(day11_input)):
    for j in range(len(day11_input[0])):
        if day11_input[i][j] == "#":
            dict_test[numero] = (i, j)
            numero += 1     

# Expand universe
def find_dot_only_rows_cols(grid):
    """
    Finds the rows and columns in a grid that contain only the '.' character.

    :param grid: A list of strings representing the grid.
    :return: A tuple of two lists (rows, cols) where rows and cols are the indices
             of the rows and columns containing only '.'
    """
    # Convert the grid into a matrix for easier processing
    matrix = [list(row) for row in grid]

    # Number of rows and columns
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Initialize lists to keep track of rows and columns with only '.'
    dot_only_rows = []
    dot_only_cols = []

    # Check each row
    for i in range(num_rows):
        if all(cell == '.' for cell in matrix[i]):
            dot_only_rows.append(i)

    # Check each column
    for j in range(num_cols):
        if all(matrix[i][j] == '.' for i in range(num_rows)):
            dot_only_cols.append(j)

    return dot_only_rows, dot_only_cols

universe = find_dot_only_rows_cols(day11_input)


# Calculate distance
total_dist = 0
for i in range((numero-1)):
    for j in range(i+1, numero):
        
        row_dist = abs(dict_test[i][0]-dict_test[j][0])
        col_dist = abs(dict_test[i][1]-dict_test[j][1])

        if dict_test[i][0] >= dict_test[j][0]:
            expand_rows = len([x for x in universe[0] if x in range(dict_test[j][0], dict_test[i][0])]) + 1000000 

        elif dict_test[i][0] < dict_test[j][0]:
            expand_rows = len([x for x in universe[0] if x in range(dict_test[i][0], dict_test[j][0])]) + 1000000 

        if dict_test[i][1] >= dict_test[j][1]:
            expand_cols = len([x for x in universe[1] if x in range(dict_test[j][1], dict_test[i][1])]) + 1000000 

        elif dict_test[i][1] < dict_test[j][1]:
            expand_cols = len([x for x in universe[1] if x in range(dict_test[i][1], dict_test[j][1])]) + 1000000 

        path = row_dist+expand_rows + col_dist+expand_cols 
        total_dist += path

print(total_dist)
