def split_to_matrices(file_path, headings):
    matrices = {}
    current_heading = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line in headings:
                current_heading = line
                matrices[current_heading] = []
            elif line and current_heading:
                # Split the line into numbers and ensure they are in groups of three
                numbers = [int(n) for n in line.split()]
                if current_heading == "seeds:":
                    matrices[current_heading].append(numbers)
                else:
                    for i in range(0, len(numbers), 3):
                        matrices[current_heading].append(numbers[i:i+3])

    return matrices

# Usage example
headings = [
    "seeds:",
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:"
]

matrices = split_to_matrices("day5/day5_input.txt", headings)
print(matrices["seeds:"])
