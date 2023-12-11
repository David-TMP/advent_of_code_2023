import numpy as np
import timeit


# PART 1 -------------------------------------------

def read_txt_part1(txt_file):
    f = open(txt_file, "r").read().splitlines()

    for i in range(len(f)):
        f[i] = f[i].split()
        f[i].pop(0)
        f[i] = [int(i) for i in f[i]]

    return f

day6_part1_input = read_txt_part1("day6/day6_input.txt")

def day6_part1(input_list):
    sol_array = [1] * (len(input_list[0]))  # Array of 1s since we're going to be multiplying all the numbers together 

    for i in range(len(input_list[0])):  # We'll always have the same elements in Time & Distance
        contador = 0
        record = input_list[1][i]

        for time in range(input_list[0][i]):
            distance = (input_list[0][i] - time) * time
            if distance > record:
                contador += 1

        sol_array[i] = contador
        
    return np.prod(sol_array)        

start = timeit.default_timer()
day6_part1_sol = day6_part1(day6_part1_input)  
elapsed_time = timeit.default_timer()-start
print("Day 6 Part 1 Run Time = ", str(elapsed_time))
print("Day 6 Part 1 Solution = ", day6_part1_sol)


# 1 2 3 4 5 6 7

# (7-initial_number)*initial_number

# 0 = 0
# 1 = 6
# 2 = 10
# 3 = 12
# 4 = 12
# 5 = 10
# 6 = 6
# 7 = 0

# 7 segundos
# 9 metros


# PART 2 -------------------------------------------

def read_txt_part2(txt_file):
    f = open(txt_file, "r").read().splitlines()

    for i in range(len(f)):
        f[i] = f[i].split()
        f[i].pop(0)
        f[i] = int("".join([str(x) for x in f[i]]))

    return f

day6_part2_input = read_txt_part2("day6/day6_input.txt")

def day6_part2(input_list):
    sol_array = [1] 
    contador = 0
    record = input_list[1]

    for time in range(input_list[0]):
        distance = (input_list[0] - time) * time
        if distance > record:
            contador += 1

    sol_array = contador
    
    return sol_array        

start = timeit.default_timer()
day6_part2_sol = day6_part2(day6_part2_input)  
elapsed_time = timeit.default_timer()-start
print("Day 6 Part 2 Run Time = ", str(elapsed_time))
print("Day 6 Part 2 Solution = ", day6_part2_sol)