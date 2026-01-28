from solution import *

def test_example_1():
    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    assert check_valid(matrix) is True, "Valid 3x3 matrix should return True"

def test_example_2():
    matrix = [[1,1,1],[1,2,3],[1,2,3]]
    assert check_valid(matrix) is False, "Row with duplicates should return False"

def test_column_duplicate():
    matrix = [[1,2], [1,3]]
    assert check_valid(matrix) is False, "Column with duplicate values should return False"

def test_single_element():
    matrix = [[1]]
    assert check_valid(matrix) is True, "Single-element matrix should return True"

def test_row_duplicate():
    matrix = [[1,1], [2,3]]
    assert check_valid(matrix) is False, "Row with duplicate values should return False"