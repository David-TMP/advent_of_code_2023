import re
import numpy as np
import pandas as pd
import sys


# PART 1

sys.setrecursionlimit(10000)

def read_txt(txt_file):
    day1_input = np.loadtxt(txt_file, dtype = "str")
    return day1_input
    # input_string = "fsdf188788jnscmpqr66sxc4j2x"

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


df = read_txt("day1_input.txt")
out = find_numbers(df)
print("Solution Part 1 = ", out)

# PART 2

# Mapping of number words to their numeric values
digits_dict = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"}

spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def extract_calibration_value(word):
    for i in range(len(spelled_numbers)):
        if spelled_numbers[i] in word:
            word = word.replace(spelled_numbers[i], spelled_numbers[i][0]+ str(i+1) + spelled_numbers[i][-1])
    
    return word

part2_data = [extract_calibration_value(x) for x in df]
part2_sol = find_numbers(part2_data)
print("Part 2 Solution = ", part2_sol)


pattern = '|'.join(re.escape(key) for key in digits_dict.keys())

# prueba = [(key, digits_dict[key]) for key in digits_dict]
# print(prueba)
# for key in digits_dict:

re.findall(pattern, "one")
prueba2 = [re.sub(key, digits_dict[key], df[0]) for key in digits_dict if re.findall(key, df[0])]
# prueba2 = [re.sub(re.findall(digits_dict.keys(), x), digits_dict[re.findall(digits_dict.keys()), x]) for x in df]


# print(prueba2)
# print(prueba2)
# test = re.sub("four", "4", df[0])
# print(test)

# def replace_number_words(text):
#     words = text.split()
#     print(words)
#     replaced_text = [str(number_words.get(word.lower(), word)) for word in words]
#     return ' '.join(replaced_text)

# # Example usage
# text = "I have one apple and two oranges."
# converted_text = replace_number_words(text)
# print(converted_text)