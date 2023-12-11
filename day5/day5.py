# import timeit

# # Path to your file
# file_path = 'day5/day5_input.txt'

# # Headings used to split the data
# headings = [
#     "seeds:",
#     "seed-to-soil map:",
#     "soil-to-fertilizer map:",
#     "fertilizer-to-water map:",
#     "water-to-light map:",
#     "light-to-temperature map:",
#     "temperature-to-humidity map:",
#     "humidity-to-location map:"
# ]

# # Function to split file content into matrices based on headings
# def split_into_matrices(file_path, headings):
#     matrices = {}
#     current_heading = None

#     with open(file_path, 'r') as file:
#         for line in file:
#             if line.strip() in headings:
#                 current_heading = line.strip()
#                 matrices[current_heading] = []
#             elif current_heading and line.strip():
#                 matrices[current_heading].append([int(num) for num in line.split()])
    
#     return matrices


# # Splitting the file content into matrices
# matrices = split_into_matrices(file_path, headings)



# # PART 1 -------------------------------------------

# def day5_part1(list_of_matrices):

#     # Seed to soil
#     soil_array = [0]* len(matrices["seeds:"][0])
#     for seed_index, seed_value in enumerate(matrices["seeds:"][0]):
#         for soil in matrices["seed-to-soil map:"]:
#             if soil[1] <= seed_value <= (soil[1]+soil[2]-1):
#                 soil_array[seed_index] = seed_value-soil[1]+soil[0]
#         if soil_array[seed_index] == 0:
#             soil_array[seed_index] = seed_value

#     # soil to fertilizer
#     fertilizer_array = [0]* len(matrices["seeds:"][0])
#     for soil_index, soil_value in enumerate(soil_array):
#         for fertilizer in matrices["soil-to-fertilizer map:"]:
#             if fertilizer[1] <= soil_value <= (fertilizer[1]+fertilizer[2]-1):
#                 fertilizer_array[soil_index] = soil_value-fertilizer[1]+fertilizer[0]
#         if fertilizer_array[soil_index] == 0:
#             fertilizer_array[soil_index] = soil_value

#     # fertilizer to water:
#     water_array = [0]* len(matrices["seeds:"][0])
#     for fertilizer_index, fertilizer_value in enumerate(fertilizer_array):
#         for water in matrices["fertilizer-to-water map:"]:
#             if water[1] <= fertilizer_value <= (water[1]+water[2]-1):
#                 water_array[fertilizer_index] = fertilizer_value-water[1]+water[0]
#         if water_array[fertilizer_index] == 0:
#             water_array[fertilizer_index] = fertilizer_value

#     # water to light:
#     light_array = [0]* len(matrices["seeds:"][0])
#     for water_index, water_value in enumerate(water_array):
#         for light in matrices["water-to-light map:"]:
#             if light[1] <= water_value <= (light[1]+light[2]-1):
#                 light_array[water_index] = water_value-light[1]+light[0]
#         if light_array[water_index] == 0:
#                 light_array[water_index] = water_value

#     # light-to-temperature map:
#     temperature_array = [0]* len(matrices["seeds:"][0])
#     for light_index, light_value in enumerate(light_array):
#         for temperature in matrices["light-to-temperature map:"]:
#             if temperature[1] <= light_value <= (temperature[1]+temperature[2]-1):
#                 temperature_array[light_index] = light_value-temperature[1]+temperature[0]
#         if temperature_array[light_index] == 0:
#                 temperature_array[light_index] = light_value

#     # temperature to humidity:
#     humidity_array = [0]* len(matrices["seeds:"][0])
#     for temperature_index, temperature_value in enumerate(temperature_array):
#         for humidity in matrices["temperature-to-humidity map:"]:
#             if humidity[1] <= temperature_value <= (humidity[1]+humidity[2]-1):
#                 humidity_array[temperature_index] = temperature_value-humidity[1]+humidity[0]
#         if humidity_array[temperature_index] == 0:
#                 humidity_array[temperature_index] = temperature_value

#     # humidity to location:
#     location_array = [0]* len(matrices["seeds:"][0])
#     for humidity_index, humidity_value in enumerate(humidity_array):
#         for location in matrices["humidity-to-location map:"]:
#             if location[1] <= humidity_value <= (location[1]+location[2]-1):
#                 location_array[humidity_index] = humidity_value-location[1]+location[0]
#         if location_array[humidity_index] == 0:
#                 location_array[humidity_index] = humidity_value

#     return min(location_array)

# start = timeit.default_timer()
# day5_part1_sol = day5_part1(matrices)  
# elapsed_time = timeit.default_timer()-start
# print("Day 4 Part 1 Run Time = ", str(elapsed_time))
# print("Day 4 Part 1 Solution = ", day5_part1_sol)


# def transform_values(values, transformation_map):
#     for value in values:
#         transformed = False
#         for mapping in transformation_map:
#             if mapping[1] <= value <= (mapping[1] + mapping[2] - 1):
#                 yield value - mapping[1] + mapping[0]
#                 transformed = True
#                 break
#         if not transformed:
#             yield value

# def day5_part1(matrices):
#     seeds = matrices["seeds:"][0]

#     soil_values = transform_values(seeds, matrices["seed-to-soil map:"])
#     fertilizer_values = transform_values(soil_values, matrices["soil-to-fertilizer map:"])
#     water_values = transform_values(fertilizer_values, matrices["fertilizer-to-water map:"])
#     light_values = transform_values(water_values, matrices["water-to-light map:"])
#     temperature_values = transform_values(light_values, matrices["light-to-temperature map:"])
#     humidity_values = transform_values(temperature_values, matrices["temperature-to-humidity map:"])
#     location_values = transform_values(humidity_values, matrices["humidity-to-location map:"])

#     return min(location_values)

# # Example usage
# # matrices = { ... }  # Define your matrices dictionary here
# # print(day5_part1(matrices))

# start = timeit.default_timer()
# day5_part1_sol = day5_part1(matrices)  
# elapsed_time = timeit.default_timer()-start
# print("Day 4 Part 1 Run Time = ", str(elapsed_time))
# print("Day 4 Part 1 Solution = ", day5_part1_sol)



# # PART 2 -------------------------------------------

# def extend_seeds_generator(seeds):
#     for i in range(0, len(seeds), 2):
#         start = seeds[i]
#         count = seeds[i + 1]
#         for val in range(start, start + count):
#             yield val

# def day5_part2(matrices):

#     matrices["seeds_new:"] = extend_seeds_generator(matrices["seeds:"][0])
#     seeds = matrices["seeds_new:"]

#     soil_values = transform_values(seeds, matrices["seed-to-soil map:"])
#     fertilizer_values = transform_values(soil_values, matrices["soil-to-fertilizer map:"])
#     water_values = transform_values(fertilizer_values, matrices["fertilizer-to-water map:"])
#     light_values = transform_values(water_values, matrices["water-to-light map:"])
#     temperature_values = transform_values(light_values, matrices["light-to-temperature map:"])
#     humidity_values = transform_values(temperature_values, matrices["temperature-to-humidity map:"])
#     location_values = transform_values(humidity_values, matrices["humidity-to-location map:"])

#     return min(location_values)

# # start = timeit.default_timer()
# # day5_part2_sol = day5_part2(matrices)  
# # elapsed_time = timeit.default_timer()-start
# # print("Day 4 Part 2 Run Time = ", str(elapsed_time))
# # print("Day 4 Part 2 Solution = ", day5_part2_sol)

# from functools import reduce

# seeds, *mappings = open('day5/day5_input.txt').read().split('\n\n')
# seeds = list(map(int, seeds.split()[1:]))

# def lookup(inputs, mapping):
#     for start, length in inputs:
#         while length > 0:
#             for m in mapping.split('\n')[1:]:
#                 dst, src, len = map(int, m.split())
#                 delta = start - src
#                 if delta in range(len):
#                     len = min(len - delta, length)
#                     yield (dst + delta, len)
#                     start += len
#                     length -= len
#                     break
#             else: yield (start, length); break

# print(*[min(reduce(lookup, mappings, s))[0] for s in [
#     zip(seeds, [1] * len(seeds)),
#     zip(seeds[0::2], seeds[1::2])]])


import sys
import re
from collections import defaultdict
D = open("day5/day5_input.txt").read().strip()
L = D.split('\n')

parts = D.split('\n\n')
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]

class Function:
  def __init__(self, S):
    lines = S.split('\n')[1:] # throw away name
    # dst src sz
    self.tuples: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]
    #print(self.tuples)
  def apply_one(self, x: int) -> int:
    for (dst, src, sz) in self.tuples:
      if src<=x<src+sz:
        return x+dst-src
    return x

  # list of [start, end) ranges
  def apply_range(self, R):
    A = []
    for (dest, src, sz) in self.tuples:
      src_end = src+sz
      NR = []
      while R:
        # [st                                     ed)
        #          [src       src_end]
        # [BEFORE ][INTER            ][AFTER        )
        (st,ed) = R.pop()
        # (src,sz) might cut (st,ed)
        before = (st,min(ed,src))
        inter = (max(st, src), min(src_end, ed))
        after = (max(src_end, st), ed)
        if before[1]>before[0]:
          NR.append(before)
        if inter[1]>inter[0]:
          A.append((inter[0]-src+dest, inter[1]-src+dest))
        if after[1]>after[0]:
          NR.append(after)
      R = NR
    return A+R

Fs = [Function(s) for s in others]

P1 = []
for x in seed:
  for f in Fs:
    x = f.apply_one(x)
  P1.append(x)
print(min(P1))

P2 = []
pairs = list(zip(seed[::2], seed[1::2]))
for st, sz in pairs:
  # inclusive on the left, exclusive on the right
  # e.g. [1,3) = [1,2]
  # length of [a,b) = b-a
  # [a,b) + [b,c) = [a,c)
  R = [(st, st+sz)]
  for f in Fs:
    R = f.apply_range(R)
  #print(len(R))
  P2.append(min(R)[0])
print(min(P2))