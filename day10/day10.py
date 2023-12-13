import timeit

# Read Input Data
def read_txt(txt_file):
    f = open(txt_file, "r")
    return f.read().splitlines()

day10_input = read_txt("day10/day10_input.txt")

# Auxiliary function
def find_s(input):
    for row, letter in enumerate(input):
        col = letter.find("S")
        if col != -1:
            return [row, col]


# PART 1 -------------------------------------------

def day10_part1(input, s_pos):

    current_row = s_pos[0] - 1  # Looking at the position of "S" we can see that we could start our path on a row above ("|")
    current_col = s_pos[1]
    previous_row = s_pos[0]
    previous_col = s_pos[1]
    contador = 1


    while current_row != s_pos[0] or current_col != s_pos[1]:

        if input[current_row][current_col] == ".":
            print("ERROR")
            exit

        if input[current_row][current_col] == "|" and previous_row == current_row+1: # You're going North
            previous_row = current_row
            current_row -= 1
            contador += 1
            continue

        if input[current_row][current_col] == "|" and previous_row == current_row-1: # You're going South
            previous_row = current_row
            current_row += 1
            contador += 1
            continue
        
        if input[current_row][current_col] == "F" and previous_row == current_row+1:  # You're going East
            previous_row = current_row
            current_col += 1
            contador += 1
            continue    
        
        if input[current_row][current_col] == "F" and previous_col == current_col+1:  # You're going South
            previous_col = current_col
            current_row += 1
            contador += 1
            continue    
        
        if input[current_row][current_col] == "-" and previous_col == current_col-1:  # You're going East
            previous_col = current_col
            current_col += 1
            contador += 1
            continue

        if input[current_row][current_col] == "-" and previous_col == current_col+1:  # You're going West
            previous_col = current_col
            current_col -= 1
            contador += 1
            continue

        if input[current_row][current_col] == "L" and previous_col == current_col+1:  # You're going North
            previous_col = current_col
            current_row -= 1
            contador += 1
            continue

        if input[current_row][current_col] == "L" and previous_row == current_row-1:  # You're going East
            previous_row = current_row
            current_col += 1
            contador += 1
            continue

        if input[current_row][current_col] == "J" and previous_col == current_col-1:  # You're going North
            previous_col = current_col
            current_row -= 1
            contador += 1
            continue

        if input[current_row][current_col] == "J" and previous_row == current_row-1:  # You're going West
            previous_row = current_row
            current_col -= 1
            contador += 1
            continue

        if input[current_row][current_col] == "7" and previous_col == current_col-1:  # You're going South
            previous_col = current_col
            current_row += 1
            contador += 1
            continue

        if input[current_row][current_col] == "7" and previous_row == current_row+1:  # You're going West
            previous_row = current_row
            current_col -= 1
            contador += 1
            continue

    return contador/2


start = timeit.default_timer()
day10_part1_sol = day10_part1(day10_input, find_s(day10_input))
elapsed_time = timeit.default_timer()-start
print("Day 10 Part 1 Run Time = ", str(elapsed_time))
print("Day 10 Part 1 Solution = ", day10_part1_sol)


# PART 2 -------------------------------------------

# PENDING!