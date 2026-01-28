from solution import *

def test_example_1():
    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    assert check_valid(matrix) is True, "Example 1 should return True"

def test_example_2():
    matrix = [[1,1,1],[1,2,3],[1,2,3]]
    assert check_valid(matrix) is False, "Example 2 should return False"

def test_single_element():
    matrix = [[1]]
    assert check_valid(matrix) is True, "Single element matrix should be valid"

def test_valid_2x2():
    matrix = [[1,2], [2,1]]
    assert check_valid(matrix) is True, "Valid 2x2 matrix should return True"

def test_invalid_row():
    matrix = [[1,1], [2,3]]
    assert check_valid(matrix) is False, "Duplicate in row should return False"