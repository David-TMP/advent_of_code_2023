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
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            return i, True
    return -1, False

# Checking all pairs beyond the centre
def check_pairs(input):
    mirror = False
    init, centre_found = find_centre(input)
    if centre_found:
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
    if mirror == False:
        return 0
    return init+1

    
day13_input_rows = split_data_by_empty_elements(read_rows("day13/day13_input.txt"))
day13_input_cols = rows_to_columns(day13_input_rows)


out_rows = [100*check_pairs(x) for x in day13_input_rows]
out_cols = [check_pairs(x) for x in day13_input_cols]

print(out_rows)
print(out_cols)
sol = out_rows+out_cols
# print(sol)