from solution import *

def test_example_1():
    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    assert checkValid(matrix) is True, "Valid Latin square should return True"

def test_example_2():
    matrix = [[1,1,1],[1,2,3],[1,2,3]]
    assert checkValid(matrix) is False, "Matrix with row/column duplicates should return False"

def test_duplicate_in_row():
    matrix = [[1,2], [1,2]]
    assert checkValid(matrix) is False, "Duplicate values in row should fail validation"

def test_single_element():
    matrix = [[1]]
    assert checkValid(matrix) is True, "Single-element matrix should be valid"

def test_duplicate_in_column():
    matrix = [[1,2], [1,3]]
    assert checkValid(matrix) is False, "Duplicate values in column should fail validation"