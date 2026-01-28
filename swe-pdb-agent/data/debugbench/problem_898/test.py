from solution import *

def test_example_1():
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    assert minimumObstacles(grid) == 2, "Failed to calculate correct minimum obstacles for example 1"

def test_example_2():
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    assert minimumObstacles(grid) == 0, "Failed to identify zero-obstacle path in example 2"

def test_single_cell_grid():
    grid = [[0]]
    assert minimumObstacles(grid) == 0, "Failed on single-cell grid"

def test_2x2_diagonal_path():
    grid = [[0,1],[1,0]]
    assert minimumObstacles(grid) == 1, "Failed to calculate minimum obstacles in 2x2 diagonal scenario"

def test_all_zeros_path():
    grid = [[0,0,0], [0,0,0], [0,0,0]]
    assert minimumObstacles(grid) == 0, "Failed to identify zero-obstacle path in all-zero grid"