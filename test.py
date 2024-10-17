def find_consecutive_ones(grid):
    results = []
    
    for row_index, row in enumerate(grid):
        count = 0  # Initialize count for consecutive 1s
        start_index = -1  # Track the start index of the consecutive 1s

        for col_index, value in enumerate(row):
            if value == 1:
                if count == 0:
                    # Found the start of a new sequence of 1s
                    start_index = col_index
                count += 1  # Increase the count for consecutive 1s
            else:
                if count > 0:
                    # We found a sequence of 1s, store the result
                    results.append((start_index, row_index, count, 1))  # (start_index, row_index, width, height)
                    count = 0  # Reset count for the next sequence

        # Check if there was a sequence of 1s at the end of the row
        if count > 0:
            results.append((start_index, row_index, count, 1))  # (start_index, row_index, width, height)

    return results

# Example 2D array
grid = [
[0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 1, 0, 0, 1, 0],
[1, 0, 0, 1, 1, 1, 0, 0, 1],
[0, 1, 0, 0, 1, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 1, 1, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0]


]

# Find and print the consecutive 1s
result = find_consecutive_ones(grid)

for line in result:
    print(f"({line[0]},{line[1]},{line[2]},{line[3]})")
