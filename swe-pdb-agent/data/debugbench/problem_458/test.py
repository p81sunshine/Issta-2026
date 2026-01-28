from solution import *

def test_example_1():
    grid = [[1,1,1],[1,0,0],[1,1,1]]
    assert isPossibleToCutPath(grid) is True, "Example 1 failed"

def test_example_2():
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    assert isPossibleToCutPath(grid) is False, "Example 2 failed"

def test_edge_case_1x1():
    grid = [[1]]
    assert isPossibleToCutPath(grid) is False, "1x1 grid edge case failed"

def test_edge_case_2x2():
    grid = [[1,1],[1,1]]
    assert isPossibleToCutPath(grid) is False, "2x2 grid edge case failed"

def test_edge_case_1x3():
    grid = [[1,1,1]]
    assert isPossibleToCutPath(grid) is True, "1x3 grid edge case failed"