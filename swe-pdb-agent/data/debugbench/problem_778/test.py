from solution import *

def test_example_1():
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    assert minimumObstacles(grid) == 2, "Should return 2 obstacles for the sample grid"

def test_example_2():
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    assert minimumObstacles(grid) == 0, "Should return 0 obstacles for unobstructed path"

def test_single_cell_grid():
    grid = [[0]]
    assert minimumObstacles(grid) == 0, "Single cell grid should require 0 obstacles"

def test_all_zero_path():
    grid = [[0 for _ in range(5)] for _ in range(5)]
    assert minimumObstacles(grid) == 0, "Grid with all zeros should have zero obstacles"

def test_obstacle_forced_path():
    grid = [[0, 1, 1],
            [1, 1, 0],
            [0, 1, 0]]
    assert minimumObstacles(grid) == 2, "Should find minimal obstacles in forced path scenario"