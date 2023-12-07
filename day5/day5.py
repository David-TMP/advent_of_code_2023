
# Path to your file
file_path = 'day5/day5_input.txt'

# Headings used to split the data
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

# Function to split file content into matrices based on headings
def split_into_matrices(file_path, headings):
    matrices = {}
    current_heading = None

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() in headings:
                current_heading = line.strip()
                matrices[current_heading] = []
            elif current_heading and line.strip():
                matrices[current_heading].append([int(num) for num in line.split()])
    
    return matrices


# Splitting the file content into matrices
matrices = split_into_matrices(file_path, headings)
print(matrices["seeds:"])

# # Example to print the first few rows of each matrix
# for heading, matrix in matrices.items():
#     print(f"{heading} First few rows:", matrix[:2], "\n")
