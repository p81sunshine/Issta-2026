from solution import *

def test_example_1():
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    assert minimumObstacles(grid) == 2, "Failed on example 1"

def test_example_2():
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    assert minimumObstacles(grid) == 0, "Failed on example 2"

def test_single_cell():
    grid = [[0]]
    assert minimumObstacles(grid) == 0, "Failed on single cell grid"

def test_clear_path():
    grid = [[0,0,0], [0,1,0], [0,0,0]]
    assert minimumObstacles(grid) == 0, "Failed to find clear path"

def test_2x2_with_one_obstacle():
    grid = [[0,1], [1,0]]
    assert minimumObstacles(grid) == 1, "Failed on 2x2 grid with one obstacle"