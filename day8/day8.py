import timeit
import math


# Read Input Data
def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract the first line as a list
    moves = lines[0].strip()

    # Process the remaining lines to create a dictionary
    nodes = {}
    for line in lines[1:]:
        line = line.strip()
        if line:  # Check if line is not empty
            key, value = line.split(' = ')
            value = tuple(value.strip('()').split(', '))
            nodes[key] = value

    return moves, nodes


file_path = 'day8/day8_input.txt'
moves, nodes = process_file(file_path)


# PART 1 -------------------------------------------

def day8_part1(initial_value, moves, nodes):

    current_value = initial_value
    iter = 0

    while current_value != 'ZZZ':

        if moves[iter % len(moves)] == 'L':
            current_value = nodes[current_value][0]
        else:
            current_value = nodes[current_value][1]
        
        iter += 1

    return iter

start = timeit.default_timer()
day8_part1_sol = day8_part1('AAA', moves, nodes)  
elapsed_time = timeit.default_timer()-start
print("Day 6 Part 1 Run Time = ", str(elapsed_time))
print("Day 6 Part 1 Solution = ", day8_part1_sol)


# PART 2 -------------------------------------------

def day8_part2(start, moves, nodes):
     
	pos = start
     
	iter = 0
     
	while not pos.endswith('Z'):
		d = moves[iter % len(moves)]
		pos = nodes[pos][0 if d=='L' else 1]
		iter += 1
	return iter


ret = 1


for start in nodes:
	if start.endswith('A'):
		ret = math.lcm(ret, day8_part2(start, moves, nodes))
print("p2", ret)