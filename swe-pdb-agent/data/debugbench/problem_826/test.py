from solution import *

def test_example_1():
    grid = [[1,1,1],[1,0,0],[1,1,1]]
    assert isPossibleToCutPath(grid) is True, "Should return True for first example"

def test_example_2():
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    assert isPossibleToCutPath(grid) is False, "Should return False for second example"

def test_single_row():
    grid = [[1,1,1]]
    assert isPossibleToCutPath(grid) is True, "Single row should return True when middle cell can be removed"

def test_2x2_grid():
    grid = [[1,1], [1,1]]
    assert isPossibleToCutPath(grid) is False, "2x2 grid should return False as no single cell removal breaks all paths"

def test_single_cell():
    grid = [[1]]
    assert isPossibleToCutPath(grid) is False, "Single cell grid should return False"