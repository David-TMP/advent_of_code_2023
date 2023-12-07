import re
import timeit

# Read Input Data
def read_txt(txt_file):
    f = open(txt_file, "r")
    return f.read().splitlines()

day3_input = read_txt("day3/day3_input.txt")


# PART 1 -------------------------------------------

# Symbols dictionary {position: symbol}
symbols = dict()
for fila, texto in enumerate(day3_input):
    for columna, character in enumerate(texto):
        if character not in "1234567890.":
            symbols[(fila, columna)] = character

def day3_part1(day3_input):
    counter = 0
    final_sum = 0

    for row in range(len(day3_input)):
        for match in re.finditer(r"\d+", day3_input[row]):
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
                final_sum = final_sum + int(day3_input[row][init_pos:end_pos])
            
            counter = 0

    return(final_sum)

start = timeit.default_timer()
day3_part1_sol = day3_part1(day3_input)  
elapsed_time = timeit.default_timer()-start
print("Day 3 Part 1 Run Time = ", str(elapsed_time))
print("Day 3 Part 1 Solution = ", day3_part1_sol)


# PART 2 -------------------------------------------

# Aterisks dictionary {position: symbol}
asterisks = dict()
for fila, texto in enumerate(day3_input):
    for columna, asterisk in enumerate(texto):
        if asterisk in "*":
            asterisks[(fila, columna)] = asterisk

def extract_number_around_position(s, position):
    # Find all numbers in the string
    numbers = re.finditer(r'\d+', s)

    for match in numbers:
        start, end = match.span()
        # Check if the given position is within the span of a number
        if start <= position < end:
            return match.group()

    # Return None if no number is found around the position
    return None

def day3_part2(day3_input):
     gear_ratio = 0
     gear_num_1 = 1
     gear_num_2 = 1
     gear_num_3 = 1
     gear_num_4 = 1
     num_touches = 0

     for i in range(len(asterisks)):
        tuple_pos = list(asterisks.keys())[i]
        row = int(tuple_pos[0])
        col = int(tuple_pos[1])

        if day3_input[row-1][col-1].isdigit():
             num_touches += 1
             gear_num_1 = int(extract_number_around_position(day3_input[row-1], col-1))

             if day3_input[row-1][col+1].isdigit() and not day3_input[row-1][col].isdigit():
                gear_num_2 = int(extract_number_around_position(day3_input[row-1], col+1))
                gear_ratio = gear_ratio + (gear_num_1 * gear_num_2 * gear_num_3 * gear_num_4)
                num_touches = 0
                gear_num_1 = 1
                gear_num_2 = 1
                gear_num_3 = 1
                gear_num_4 = 1
                continue

        elif day3_input[row-1][col].isdigit():
             num_touches += 1             
             gear_num_1 = int(extract_number_around_position(day3_input[row-1], col))

        elif day3_input[row-1][col+1].isdigit():
             gear_num_1 = int(extract_number_around_position(day3_input[row-1], col+1))
             num_touches += 1
                                 
        if day3_input[row+1][col-1].isdigit():
             gear_num_2 = int(extract_number_around_position(day3_input[row+1], col-1))
             num_touches += 1
             
             if day3_input[row+1][col+1].isdigit() and not day3_input[row+1][col].isdigit():
                gear_num_3 = int(extract_number_around_position(day3_input[row+1], col+1))
                gear_ratio = gear_ratio + (gear_num_1 * gear_num_2 * gear_num_3 * gear_num_4)
                num_touches = 0
                gear_num_1 = 1
                gear_num_2 = 1
                gear_num_3 = 1
                gear_num_4 = 1
                continue

        elif day3_input[row+1][col].isdigit():
             gear_num_2 = int(extract_number_around_position(day3_input[row+1], col))
             num_touches += 1
             
        elif day3_input[row+1][col+1].isdigit():
             gear_num_2 = int(extract_number_around_position(day3_input[row+1], col+1))
             num_touches += 1

        if day3_input[row][col-1].isdigit():
             gear_num_3 = int(extract_number_around_position(day3_input[row], col-1))
             num_touches += 1

        if day3_input[row][col+1].isdigit():
             gear_num_4 = int(extract_number_around_position(day3_input[row], col+1))
             num_touches += 1
             
        if num_touches >= 2:
             gear_ratio = gear_ratio + (gear_num_1 * gear_num_2 * gear_num_3 * gear_num_4)

        num_touches = 0
        gear_num_1 = 1
        gear_num_2 = 1
        gear_num_3 = 1
        gear_num_4 = 1

     return(gear_ratio)

start = timeit.default_timer()
day3_part2_sol = day3_part2(day3_input)  
elapsed_time = timeit.default_timer()-start
print("Day 3 Part 2 Run Time = ", str(elapsed_time))
print("Day 3 Part 2 Solution = ", day3_part2_sol)