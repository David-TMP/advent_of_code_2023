import timeit

# Read input as rows
def read_input(txt_file):
    f = open(txt_file, "r")
    matrix = [list(row) for row in f.read().strip().split("\n")]
    return matrix


day14_input = read_input("day14/day14_input.txt")

start = timeit.default_timer()
for x in range(1, 10000):
    for i in range(1, len(day14_input)):
        for j in range(len(day14_input)):
            index = i
            while(index > 0 and day14_input[index][j] == "O" and day14_input[index-1][j] == "."):
                day14_input[index][j] = "."
                day14_input[index-1][j] = "O"
                index -= 1

elapse = timeit.default_timer()-start
print(elapse)


def count_zeros(array):
    # Initialize an empty list to store the count of 'O's in each row
    counts = []
    
    # Iterate through each row in the array
    for row in array:
        # Count the number of 'O's in the row and add it to the counts list
        counts.append(row.count('O'))
    
    return counts

import numpy as np
count = count_zeros(day14_input)
sol = [x+1 for x in reversed(range(len(day14_input)))]  

final = np.multiply(count, sol).sum()
# print(final)