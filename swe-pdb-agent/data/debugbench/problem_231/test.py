from solution import *

def test_example_1():
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    assert minimumObstacles(grid) == 2, "Should return 2 for the first example"

def test_example_2():
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    assert minimumObstacles(grid) == 0, "Should return 0 for the second example"

def test_edge_case_single_cell():
    grid = [[0]]
    assert minimumObstacles(grid) == 0, "Single cell grid should return 0"

def test_strictly_clear_path():
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert minimumObstacles(grid) == 0, "All-clear grid should return 0"