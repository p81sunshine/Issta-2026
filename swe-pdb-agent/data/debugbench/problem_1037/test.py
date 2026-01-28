from solution import *

def test_example_1():
    grid = [[1,1,1],[1,0,0],[1,1,1]]
    assert isPossibleToCutPath(grid) is True, "Example 1 failed"

def test_example_2():
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    assert isPossibleToCutPath(grid) is False, "Example 2 failed"

def test_two_paths_case():
    grid = [[1,1],[1,1]]
    assert isPossibleToCutPath(grid) is False, "Two paths case failed"

def test_single_column_path():
    grid = [[1], [1], [1]]
    assert isPossibleToCutPath(grid) is True, "Single column path failed"