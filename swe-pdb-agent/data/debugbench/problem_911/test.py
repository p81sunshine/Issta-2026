from solution import *

def test_example_1():
    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    assert check_valid(matrix) is True, "Valid 3x3 matrix should return True"

def test_example_2():
    matrix = [[1,1,1],[1,2,3],[1,2,3]]
    assert check_valid(matrix) is False, "Duplicate values in rows/columns should return False"

def test_duplicate_in_columns():
    matrix = [[1,2], [1,2]]
    assert check_valid(matrix) is False, "Duplicate values in columns should return False"

def test_out_of_bounds_value():
    matrix = [[1,2,4], [3,4,2], [2,3,1]]
    assert check_valid(matrix) is False, "Value 4 in 3x3 matrix is out of bounds"

def test_empty_matrix():
    matrix = []
    assert check_valid(matrix) is True, "Empty matrix should return True"