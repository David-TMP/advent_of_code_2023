def count_arrangements(springs, group_sizes):
    def dp(index, group_index, broken_count):
        # Base case: reached the end of the string and processed all groups
        if index == len(springs) and group_index == len(group_sizes):
            return 1 if broken_count == 0 else 0
        if index == len(springs) or group_index == len(group_sizes):
            return 0

        # If already computed, return cached value
        if (index, group_index, broken_count) in memo:
            return memo[(index, group_index, broken_count)]

        count = 0
        current_group_size = group_sizes[group_index]

        # Handling operational, broken, or unknown conditions
        if springs[index] == '.' or springs[index] == '?':
            # Operational: if current group is completed, move to next group
            if broken_count == current_group_size:
                count += dp(index + 1, group_index + 1, 0)
            else:
                count += dp(index + 1, group_index, broken_count)

        if springs[index] == '#' or springs[index] == '?':
            # Broken: if adding a broken spring doesn't exceed current group size
            if broken_count < current_group_size:
                count += dp(index + 1, group_index, broken_count + 1)

        memo[(index, group_index, broken_count)] = count
        return count

    memo = {}
    return dp(0, 0, 0)

# Parse the input and apply the function to each row
input_data = [
    "???.### 1,1,3",
    ".??..??...?##. 1,1,3",
    "?#?#?#?#?#?#?#? 1,3,1,6",
    "????.#...#... 4,1,1",
    "????.######..#####. 1,6,5",
    "?###???????? 3,2,1"
]

# Testing the modified function with the same input data
total_arrangements = 0
for row in input_data:
    springs, sizes = row.split()
    group_sizes = list(map(int, sizes.split(',')))
    total_arrangements += count_arrangements(springs, group_sizes)

print(total_arrangements)

