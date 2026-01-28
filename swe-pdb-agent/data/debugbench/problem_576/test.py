from solution import *

def test_example_1():
    assert check_valid([[1,2,3],[3,1,2],[2,3,1]]) is True, "Valid matrix should return True"

def test_example_2():
    assert check_valid([[1,1,1],[1,2,3],[1,2,3]]) is False, "Matrix with duplicates in row and column should return False"

def test_single_cell():
    assert check_valid([[1]]) is True, "Single cell matrix should return True"

def test_invalid_value_zero():
    assert check_valid([[0, 2], [3, 4]]) is False, "Matrix with value 0 should return False"

def test_duplicate_in_column():
    assert check_valid([[1,2], [1,3]]) is False, "Matrix with duplicate in column should return False"