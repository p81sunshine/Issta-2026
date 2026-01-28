def is_valid_sudoku(board):
    """
    Checks if a Sudoku board is valid.

    A valid Sudoku board must satisfy the following conditions:
    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3x3 sub-boxes must also contain the digits 1-9 without repetition.

    Args:
        board (list of lists): A 9x9 Sudoku board, where empty cells are denoted by 0.

    Returns:
        bool: True if the board is valid, False otherwise.
    """

    # Check each row for validity
    for row in board:
        if not is_valid_group(row):
            return False

    # Check each column for validity
    for col in zip(*board):
        if not is_valid_group(col):
            return False

    # Check each 3x3 sub-box for validity
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_group(sub_box):
                return False

    return True


def is_valid_group(group):
    """
    Checks if a group (row, column, or 3x3 sub-box) is valid.

    A valid group must contain the digits 1-9 without repetition, and must
    not contain any zeros (empty cells).

    Args:
        group (list): The group to check.

    Returns:
        bool: True if the group is valid, False otherwise.
    """
    return len(group) == len(set(group)) and all(x in range(1, 10) for x in group)


# Test the function