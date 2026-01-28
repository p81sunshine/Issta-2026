from solution import *

def test_example_1():
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    assert minimumObstacles(grid) == 2, "Example 1: Expected 2 obstacles"

def test_example_2():
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    assert minimumObstacles(grid) == 0, "Example 2: Expected 0 obstacles"

def test_edge_single_cell():
    grid = [[0]]
    assert minimumObstacles(grid) == 0, "Edge case: Single cell grid"

def test_path_with_invalid_moves():
    grid = [[0,0,0], [1,1,0], [0,0,0]]
    assert minimumObstacles(grid) == 0, "Path through valid moves should avoid obstacles"