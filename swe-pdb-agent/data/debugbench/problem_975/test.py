from solution import *

def test_example_1():
    grid = [[1,2,4],[3,3,1]]
    assert deleteGreatestValue(grid) == 8, "Failed for example 1"

def test_example_2():
    grid = [[10]]
    assert deleteGreatestValue(grid) == 10, "Failed for example 2"

def test_two_rows_two_cols():
    grid = [[1,3],[2,4]]
    assert deleteGreatestValue(grid) == 6, "Failed for 2x2 grid"

def test_one_row():
    grid = [[1,2,3]]
    assert deleteGreatestValue(grid) == 6, "Failed for single row case"

def test_all_same_values():
    grid = [[5,5], [5,5]]
    assert deleteGreatestValue(grid) == 10, "Failed for all same values case"