import re
import numpy as np
import pandas as pd
import sys

# PART 1 -------------------------------------------

# def read_txt(txt_file):
#     f = open(txt_file, "r")
#     return f.read().splitlines()

# day3_input = read_txt("day3/day3_input.txt")
# print(day3_input[1][2])

# def find_valid_numbers(input_list):
#     for i in range(len(input_list)):
#         for j in range(len(input_list[1])):  # All have the same length (= 140)
#             if (input_list[i][j].isnumeric()) and (not(input_list[i][j+1].isnumeric())):

#                 continue

import math as m, re

board = list(open('day3/day3_input.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

print(chars)

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))

