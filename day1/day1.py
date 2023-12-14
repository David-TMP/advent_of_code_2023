import re
import numpy as np
import sys


# PART 1 -------------------------------------------

sys.setrecursionlimit(10000)

def read_txt(txt_file):
    day1_input = np.loadtxt(txt_file, dtype = "str")
    return day1_input

def find_numbers(input_data):

    if len(input_data) == 0:
        return 0

    # Define a regular expression pattern to match a digit
    pattern = r'\d'

    # Use re.findall to find all matches in the string
    matches = re.findall(pattern, input_data[0])

    # Check if any matches are found
    if matches:
        # Access the last matched digit
        first_digit = matches[0]
        last_digit = matches[-1]
        return int(str(first_digit)+str(last_digit)) + find_numbers(input_data[1:])
    else:
        print("No digit found in the string.")
        return find_numbers(input_data[1:])


df = read_txt("day1/day1_input.txt")
out = find_numbers(df)
print("Part 1 Solution = ", out)


# PART 2 -------------------------------------------

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def extract_calibration_value(word):
    for i in range(len(numbers)):
        if numbers[i] in word:
            word = word.replace(numbers[i], numbers[i][0]+ str(i+1) + numbers[i][-1])
    
    return word

part2_data = [extract_calibration_value(x) for x in df]
part2_sol = find_numbers(part2_data)
print("Part 2 Solution = ", part2_sol)