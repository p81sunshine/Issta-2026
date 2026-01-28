def longest_connected_path(n, grid):
    """
    Returns the length of the longest connected path of same values in the grid.
    """
    def check_sequence(sequence):
        max_length = 0
        current_length = 1
        
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i - 1]:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        
        max_length = max(max_length, current_length)
        return max_length

    # Track the longest path found
    max_path_length = 0
    
    # Check all rows
    for row in grid:
        max_path_length = max(max_path_length, check_sequence(row))
    
    # Check all columns
    for col_idx in range(n):
        column = [grid[row_idx][col_idx] for row_idx in range(n)]
        max_path_length = max(max_path_length, check_sequence(column))
    
    return max_path_length - 1

# Example usage:
n = 4
gird = [
    '.X..',
    '.X..',
    '..X.',
    '....'
]
print(longest_connected_path(n, gird))  # Output: 4

n = 5
gird = [
    'X....',
    '.XX..',
    '..X..',
    '....X',
    'XXXXX'
]
print(longest_connected_path(n, gird))  # Output: 5