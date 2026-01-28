from solution import *

def test_example_1():
    grid = [[1,1,1],[1,0,0],[1,1,1]]
    assert isPossibleToCutPath(grid) is True, "Example 1 should return True"

def test_example_2():
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    assert isPossibleToCutPath(grid) is False, "Example 2 should return False"

def test_straight_line_path():
    grid = [[1,1,1]]
    assert isPossibleToCutPath(grid) is True, "Single row path should be cuttable"

def test_2x2_grid():
    grid = [[1,1], [1,1]]
    assert isPossibleToCutPath(grid) is False, "2x2 grid with two paths should not be cuttable"

def test_single_cell_edge_case():
    grid = [[1]]
    assert isPossibleToCutPath(grid) is False, "Single cell grid should not be cuttable"