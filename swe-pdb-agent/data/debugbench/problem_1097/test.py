from solution import *

def test_example_1():
    grid = [[1,2,4],[3,3,1]]
    assert deleteGreatestValue(grid) == 8, "Example 1 failed"

def test_example_2():
    grid = [[10]]
    assert deleteGreatestValue(grid) == 10, "Example 2 failed"

def test_single_row():
    grid = [[1,2,3]]
    expected = 6  # 3 + 2 + 1
    assert deleteGreatestValue(grid) == expected, "Single row test failed"

def test_two_rows_three_cols():
    grid = [[1,5,6], [2,3,4]]
    expected = 13
    assert deleteGreatestValue(grid) == expected, "Two rows three cols failed"

def test_edge_case_two_cols():
    grid = [[1,3], [2,4]]
    assert deleteGreatestValue(grid) == 6, "Edge case two cols failed"