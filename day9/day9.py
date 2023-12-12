# Libraries
import numpy as np
import timeit
from numpy.polynomial.polynomial import Polynomial

# Read Input Data
def read_txt(txt_file):
    f = open(txt_file, "r")
    return f.read().splitlines()

day9_input = read_txt("day9/day9_input.txt")


# PART 1 -------------------------------------------

def predict_lagrange(sequence, part2 = False):

    # Generate x values corresponding to the sequence indices
    y_values = list(map(int, sequence.split()))
    x_values = list(range(1, len(y_values) + 1))

    # Use Polynomial.fit to find the interpolating polynomial
    # Polynomial.fit takes in x values, y values and the degree of the polynomial
    # We use degree len(sequence) - 1 because we have that many points
    lagrange_poly = Polynomial.fit(x_values, y_values, len(y_values) - 1)

    # Predict the next value by evaluating the polynomial at the next x value
    # OR the value before the first if Part2 is TRUE
    if part2 == False:
        next_value = lagrange_poly(len(y_values)+1)
    elif part2 == True:
        next_value = lagrange_poly(0)

    return next_value

start = timeit.default_timer()
day9_part1_sol = sum([round(predict_lagrange(day9_input[i])) for i in range(len(day9_input))])
elapsed_time = timeit.default_timer()-start
print("Day 9 Part 1 Run Time = ", str(elapsed_time))
print("Day 9 Part 1 Solution = ", day9_part1_sol)


# PART 2 -------------------------------------------

start = timeit.default_timer()
day9_part2_sol = sum([round(predict_lagrange(day9_input[i], part2=True)) for i in range(len(day9_input))])
elapsed_time = timeit.default_timer()-start
print("Day 9 Part 2 Run Time = ", str(elapsed_time))
print("Day 9 Part 2 Solution = ", day9_part2_sol)
