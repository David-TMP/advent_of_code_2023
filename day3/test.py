import re
from collections import defaultdict
from math import prod

# PART 1 -------------------------------------------

# Read Input Data
def read_txt(txt_file):
    f = open(txt_file, "r")
    return f.read().splitlines()

day3_input = read_txt("day3/day3_input.txt")

# Symbols dictionary {xy_position: symbol}
symbols = dict()
for fila, texto in enumerate(day3_input):
    for columna, character in enumerate(texto):
        if character not in "1234567890.":
            symbols[(fila, columna)] = character

prueba = (119, 1)
print(list(symbols.keys())[5] == prueba)
# print(symbols["(6, 1)"])
# print(symbols[(2,1)])
    # for match in re.finditer(r"\d+", line):

print(day3_input[139][135:138])

def debugeando():
    counter = 0
    final_sum = 0

    for row in range(len(day3_input)):
        for match in re.finditer(r"\d+", day3_input[row]):
            # print(type(match.start()))
            # for i in range(len(symbols)):
            # print(match.start())
            # print(match.end())
            try:
                if symbols[(row, match.start()-1)]:
                    counter += 1
            except KeyError:
                    pass
            try:
                if symbols[(row, match.start()+1)]:
                    counter += 1
            except KeyError:
                    pass
            try:
                if symbols[(row-1, match.start()-1)]:
                    counter += 1
            except KeyError:
                    pass
            try:
                if symbols[(row-1, match.start())]:
                    counter += 1
            except KeyError:
                    pass
            try:
                if symbols[(row-1, match.start()+1)]:
                    counter += 1
            except KeyError:
                    pass
            try:
                if symbols[(row+1, match.start()-1)]:
                    counter += 1
            except KeyError:
                    pass
            try:
                if symbols[(row+1, match.start())]:
                    counter += 1
            except KeyError:
                    pass
            try:
                if symbols[(row+1, match.start()+1)]:
                    counter += 1
            except KeyError:
                    pass
            try:
                if symbols[(row+1, match.end()-1)]:
                    counter += 1
            except KeyError:
                    pass
            try:
                if symbols[(row-1, match.end()-1)]:
                    counter += 1
            except KeyError:
                    pass
            try:
                if symbols[(row+1, match.end())]:
                    counter += 1
            except KeyError:
                    pass
            try:
                if symbols[(row, match.end())]:
                    counter += 1
            except KeyError:
                    pass
            try:
                if symbols[(row-1, match.end())]:
                    counter += 1
            except KeyError:
                    pass
            
            if counter > 0:
                init_pos = int(match.start())
                end_pos = int(match.end())
                # print(end_pos)
                final_sum = final_sum + int(day3_input[row][init_pos:end_pos])
            
            counter = 0

    print(final_sum)

debugeando()  
        # == (match.start()-1, row) \
        # or symbols[i] == (match.start(), row+1) \
        # or symbols[i] == (match.start(), row-1) \
        # or symbols[i] == (match.start()+1, row+1) \
        # or symbols[i] == (match.start()+1, row-1) \
        # or symbols[i] == (match.start()-1, row+1) \
        # or symbols[i] == (match.start()-1, row-1) \
        # or symbols[i] == (match.end()+1, row) \
        # or symbols[i] == (match.end()+1, row+1) \
        # or symbols[i] == (match.end()+1, row-1):
                # print(day3_input[1][match.start()])    

# # checking if a number has a rectangular neighborhood containing a symbol and
# # building a gear grid as {gear_position: [part numbers list]}
# gears = defaultdict(list)
# print(gears)
# part_numbers_sum = 0
# for y, line in enumerate(day3_input):
#     for match in re.finditer(r"\d+", line):
#         for (s_x, s_y), c in symbols.items():
#             if (match.start() - 1 <= s_x <= match.end()) and (y - 1 <= s_y <= y + 1):
#                 num = int(match.group())
#                 part_numbers_sum += num
#                 if c == "*":
#                     gears[(s_x, s_y)].append(num)
#                 break

# # ========= PART 1 =========
# print(part_numbers_sum)

# # ========= PART 2 =========
# print(sum(prod(part_nums) for part_nums in gears.values() if len(part_nums) == 2))
