import timeit

# Read input as rows
def read_rows(txt_file):
    f = open(txt_file, "r")
    return f.read().splitlines()

# Transpose data (rows to columns)
def rows_to_columns(rows):
    columns = list()

    for grid in range(len(rows)):
        column = [''] * len(rows[grid][0])
        for line in rows[grid]:
            for i in range(len(line)):
                column[i] += line[i]

        columns.append(column)

    return columns

# Splitting array into lists
def split_data_by_empty_elements(data):
    split_lists = []
    current_list = []

    for element in data:
        if element == '':
            if current_list:
                split_lists.append(current_list)
                current_list = []
        else:
            current_list.append(element)

    if current_list:
        split_lists.append(current_list)

    return split_lists


# Finding the centre where the mirror starts
def find_centre(input):
    centre_pos = list()
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            centre_pos.append(i)
    if not centre_pos:  # Empty list, no position found
        return [], False
    else:
        return centre_pos, True

# Checking all pairs beyond the centre
def check_pairs(input):
    mirror = False
    all_init_pos, centre_found = find_centre(input)
    if centre_found:
        for init in all_init_pos: 
            index_left = init-1
            index_right = init+2
            mirror = True
            while index_left >= 0 and index_right < len(input):
                if input[index_left] == input[index_right]:
                    index_left -= 1
                    index_right += 1
                    continue
                else:
                    mirror = False
                    break
            if mirror == True:
                return init+1
    if mirror == False:
        return 0
    return init+1


# PART 1 -------------------------------------------

day13_input_rows = split_data_by_empty_elements(read_rows("day13/day13_input_test2.txt"))
day13_input_cols = rows_to_columns(day13_input_rows)

start = timeit.default_timer()
out_rows = sum([100*check_pairs(x) for x in day13_input_rows])
out_cols = sum([check_pairs(x) for x in day13_input_cols])
day13_part1_sol = out_rows+out_cols 
elapsed_time = timeit.default_timer()-start
print("Day 13 Part 1 Run Time = ", str(elapsed_time))
print("Day 13 Part 1 Solution = ", day13_part1_sol)


# PART 2 -------------------------------------------

# Compares two strings and returns True if they differ by exactly one character.
def compare_strings(str1, str2):

    if len(str1) != len(str2):
        return False

    differences = [i for i in range(len(str1)) if str1[i] != str2[i]]

    if len(differences) == 1:
        return True
    else:
        return False

def find_smudge_centre(input):
    centre_pos = list()
    for i in range(len(input)-1):
        smudged_found = compare_strings(input[i], input[i+1])
        if smudged_found:
            centre_pos.append(i)
    if not centre_pos:  # Empty list, no position found
        return [], False
    else:
        return centre_pos, True
    
# Checking all pairs beyond the centre
def check_pairs_part2(input):
    mirror = False
    init_pos, centre_found_original = find_centre(input)
    init_pos_smudge, centre_found_smudge = find_smudge_centre(input)
    all_init_pos = init_pos + init_pos_smudge
    if centre_found_smudge or centre_found_original:
        for init in all_init_pos: 
            index_left = init-1
            index_right = init+2
            mirror = True
            while index_left >= 0 and index_right < len(input):
                if input[index_left] == input[index_right]:
                    index_left -= 1
                    index_right += 1
                    continue
                else:
                    mirror = False
                    break
            if mirror == True:
                return init+1
    if mirror == False:
        return 0
    return init+1

start = timeit.default_timer()
out_rows = sum([100*check_pairs_part2(x) for x in day13_input_rows])
out_cols = sum([check_pairs_part2(x) for x in day13_input_cols])
day13_part2_sol = out_rows+out_cols 
elapsed_time = timeit.default_timer()-start
print("Day 13 Part 2 Run Time = ", str(elapsed_time))
print("Day 13 Part 2 Solution = ", day13_part2_sol)