import re
import timeit
import numpy as np

# Read Input Data
def read_txt(txt_file):
    f = open(txt_file, "r")
    return f.read().splitlines()

day4_input = read_txt("day4/day4_input.txt")

# AUX FUNCTIONS -------------------------------------------

def clean_day4_data(day4_input):

    card_number = np.empty(len(day4_input), dtype=object)
    winning_numbers = np.empty(shape=(len(day4_input), 10), dtype=object) 
    numbers_you_have = np.empty(shape=(len(day4_input), 25), dtype=object)

    for i in range(len(day4_input)):
        numbers_before_pipe = re.findall(r'\d+', day4_input[i].split('|')[0])
        numbers_before_pipe = [int(num) for num in numbers_before_pipe]
        numbers_after_pipe = re.findall(r'\d+', day4_input[i].split('|')[1])
        numbers_after_pipe = [int(num) for num in numbers_after_pipe]
        card_number[i] = numbers_before_pipe.pop(0)
        numbers_before_pipe.sort()
        winning_numbers[i] = numbers_before_pipe
        numbers_you_have[i] = numbers_after_pipe
    
    return {"card_id": card_number,
            "winning_numbers": winning_numbers,
            "numbers_you_have": numbers_you_have,
            "points_worth": [1] * len(day4_input)}

# Binary Search function
def binary_search(array, x, low, high):

    if high >= low:
        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binary_search(array, x, low, mid-1)

        # Search the right half
        else:
            return binary_search(array, x, mid + 1, high)

    else:
        return -1



# PART 1 -------------------------------------------

def day4_part1(day4_input):
    contador = -1
    day4_input_clean = clean_day4_data(day4_input)

    for row in range(len(day4_input)):
        for col in range(day4_input_clean["numbers_you_have"].shape[1]):
            num_to_search = day4_input_clean["numbers_you_have"][row][col]
            if binary_search(day4_input_clean["winning_numbers"][row], num_to_search, 0, len(day4_input_clean["winning_numbers"][row])-1) != -1:
                contador += 1
        if contador == -1:
            day4_input_clean["points_worth"][row] = 0
        elif contador >= 0:
            day4_input_clean["points_worth"][row] = 2 ** contador
            contador = -1
                
    return(sum(day4_input_clean["points_worth"]))

    
start = timeit.default_timer()
day4_part1_sol = day4_part1(day4_input)  
elapsed_time = timeit.default_timer()-start
print("Day 4 Part 1 Run Time = ", str(elapsed_time))
print("Day 4 Part 1 Solution = ", day4_part1_sol)


# PART 2 -------------------------------------------

def day4_part2(day4_input):
    contador = 0
    day4_input_clean = clean_day4_data(day4_input)

    for row in range(len(day4_input)):
        for col in range(day4_input_clean["numbers_you_have"].shape[1]):
            num_to_search = day4_input_clean["numbers_you_have"][row][col]
            if binary_search(day4_input_clean["winning_numbers"][row], num_to_search, 0, len(day4_input_clean["winning_numbers"][row])-1) != -1:
                contador += 1

        for i in range(contador):
            day4_input_clean["points_worth"][row + i + 1] += day4_input_clean["points_worth"][row]

        contador = 0
                
    return(sum(day4_input_clean["points_worth"]))

start = timeit.default_timer()
day4_part2_sol = day4_part2(day4_input)  
elapsed_time = timeit.default_timer()-start
print("Day 4 Part 2 Run Time = ", str(elapsed_time))
print("Day 4 Part 2 Solution = ", day4_part2_sol)
