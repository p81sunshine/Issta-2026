from solution import *

def test_example_1():
    grid = [[1,1,1],[1,0,0],[1,1,1]]
    assert isPossibleToCutPath(grid) is True, "Example 1 failed"

def test_example_2():
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    assert isPossibleToCutPath(grid) is False, "Example 2 failed"

def test_single_path_grid():
    grid = [[1,1], [1,1]]
    assert isPossibleToCutPath(grid) is False, "Single path grid test failed"