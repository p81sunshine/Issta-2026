from solution import *

def test_example_1():
    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    assert check_valid(matrix) is True, "Example 1 should return True"

def test_example_2():
    matrix = [[1,1,1],[1,2,3],[1,2,3]]
    assert check_valid(matrix) is False, "Example 2 should return False"

def test_duplicate_in_row_and_col():
    matrix = [[1,2], [1,2]]
    assert check_valid(matrix) is False, "Duplicate values in row and column should return False"

def test_single_element():
    matrix = [[1]]
    assert check_valid(matrix) is True, "Single element matrix should return True"

def test_invalid_value():
    matrix = [[1,2], [3,4]]
    assert check_valid(matrix) is False, "Matrix with values exceeding dimensions should return False"