from solution import *

def test_example_1():
    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    assert checkValid(matrix) is True, "Valid 3x3 matrix should return True"

def test_example_2():
    matrix = [[1,1,1],[1,2,3],[1,2,3]]
    assert checkValid(matrix) is False, "Matrix with duplicate values should return False"

def test_edge_case_single_element():
    matrix = [[1]]
    assert checkValid(matrix) is True, "Single-element matrix should return True"

def test_valid_2x2_matrix():
    matrix = [[1,2],[2,1]]
    assert checkValid(matrix) is True, "Valid 2x2 Latin square should return True"

def test_invalid_duplicate_row():
    matrix = [[1,2,3],[1,2,3],[3,2,1]]
    assert checkValid(matrix) is False, "Matrix with identical rows should return False"