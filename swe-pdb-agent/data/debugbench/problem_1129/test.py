from solution import *

def test_example_1():
    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    assert check_valid(matrix) is True, "Valid 3x3 Latin square should return True"

def test_example_2():
    matrix = [[1,1,1],[1,2,3],[1,2,3]]
    assert check_valid(matrix) is False, "Matrix with duplicate values in row/column should return False"

def test_2x2_valid():
    matrix = [[2,1], [1,2]]
    assert check_valid(matrix) is True, "Valid 2x2 Latin square should return True"

def test_2x2_invalid():
    matrix = [[1,1], [2,2]]
    assert check_valid(matrix) is False, "2x2 matrix with duplicate values should return False"

def test_1x1():
    matrix = [[1]]
    assert check_valid(matrix) is True, "1x1 matrix should return True"