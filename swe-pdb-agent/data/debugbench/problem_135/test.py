from solution import *

def test_example_1():
    grid = [[1,2,4],[3,3,1]]
    assert deleteGreatestValue(grid) == 8, "Example 1 should return 8"

def test_example_2():
    grid = [[10]]
    assert deleteGreatestValue(grid) == 10, "Example 2 should return 10"

def test_single_row():
    grid = [[1,2,3]]
    assert deleteGreatestValue(grid) == 6, "Single row should sum 3+2+1=6"

def test_single_column():
    grid = [[5], [7]]
    assert deleteGreatestValue(grid) == 7, "Single column should sum 7 only"