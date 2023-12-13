# Libraries
import timeit

# Read Input Data
def read_txt(txt_file):
    f = open(txt_file, "r")
    return f.read().splitlines()

day11_input = read_txt("day11/day11_input.txt")


# AUXILIARY FUNCTIONS

# Create dictionary
def find_universe_position(grid):
    uni_pos = dict()
    numero = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                uni_pos[numero] = (i, j)
                numero += 1
    return uni_pos, numero

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


# PART 1 -------------------------------------------

def day11_part1(uni_pos, uni_num, uni_empty):

    total_dist = 0
    for i in range((uni_num-1)):
        for j in range(i+1, uni_num):
            
            row_dist = abs(uni_pos[i][0]-uni_pos[j][0])
            col_dist = abs(uni_pos[i][1]-uni_pos[j][1])

            if uni_pos[i][0] >= uni_pos[j][0]:
                expand_rows = len([x for x in uni_empty[0] if x in range(uni_pos[j][0], uni_pos[i][0])]) 

            elif uni_pos[i][0] < uni_pos[j][0]:
                expand_rows = len([x for x in uni_empty[0] if x in range(uni_pos[i][0], uni_pos[j][0])])

            if uni_pos[i][1] >= uni_pos[j][1]:
                expand_cols = len([x for x in uni_empty[1] if x in range(uni_pos[j][1], uni_pos[i][1])])

            elif uni_pos[i][1] < uni_pos[j][1]:
                expand_cols = len([x for x in uni_empty[1] if x in range(uni_pos[i][1], uni_pos[j][1])])

            path = row_dist+expand_rows + col_dist+expand_cols 
            total_dist += path

    return total_dist

start = timeit.default_timer()
uni_pos, uni_num = find_universe_position(day11_input)
uni_empty = find_dot_only_rows_cols(day11_input)
day11_part1_sol = day11_part1(uni_pos, uni_num, uni_empty)
elapsed_time = timeit.default_timer()-start
print("Day 11 Part 1 Run Time = ", str(elapsed_time))
print("Day 11 Part 1 Solution = ", day11_part1_sol)


# PART 2 -------------------------------------------

def day11_part2(uni_pos, uni_num, uni_empty):

    total_dist = 0
    for i in range((uni_num-1)):
        for j in range(i+1, uni_num):
            
            row_dist = abs(uni_pos[i][0]-uni_pos[j][0])
            col_dist = abs(uni_pos[i][1]-uni_pos[j][1])

            if uni_pos[i][0] >= uni_pos[j][0]:
                expand_rows = len([x for x in uni_empty[0] if x in range(uni_pos[j][0], uni_pos[i][0])]) * (1000000-1) 

            elif uni_pos[i][0] < uni_pos[j][0]:
                expand_rows = len([x for x in uni_empty[0] if x in range(uni_pos[i][0], uni_pos[j][0])]) * (1000000-1) 

            if uni_pos[i][1] >= uni_pos[j][1]:
                expand_cols = len([x for x in uni_empty[1] if x in range(uni_pos[j][1], uni_pos[i][1])]) * (1000000-1) 

            elif uni_pos[i][1] < uni_pos[j][1]:
                expand_cols = len([x for x in uni_empty[1] if x in range(uni_pos[i][1], uni_pos[j][1])]) * (1000000-1) 

            path = row_dist+expand_rows + col_dist+expand_cols 
            total_dist += path

    return total_dist

start = timeit.default_timer()
uni_pos, uni_num = find_universe_position(day11_input)
uni_empty = find_dot_only_rows_cols(day11_input)
day11_part2_sol = day11_part2(uni_pos, uni_num, uni_empty)
elapsed_time = timeit.default_timer()-start
print("Day 11 Part 2 Run Time = ", str(elapsed_time))
print("Day 11 Part 2 Solution = ", day11_part2_sol)