from solution import *

def test_example_1():
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    assert minimumObstacles(grid) == 2, "Failed for 3x3 grid with obstacles"

def test_example_2():
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    assert minimumObstacles(grid) == 0, "Failed for grid with zero obstacles"

def test_single_cell():
    grid = [[0]]
    assert minimumObstacles(grid) == 0, "Failed for single-cell grid"

def test_all_ones():
    grid = [[1,1],[1,1]]
    assert minimumObstacles(grid) == 2, "Failed for grid with all obstacles"

def test_obstacle_in_only_path():
    grid = [[0,1,0]]
    assert minimumObstacles(grid) == 1, "Failed for row with obstacle in path"