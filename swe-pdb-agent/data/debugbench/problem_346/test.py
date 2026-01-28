from solution import *

def test_example_1():
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    assert minimumObstacles(grid) == 2, "Failed to calculate correct minimum obstacles for example 1"

def test_example_2():
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    assert minimumObstacles(grid) == 0, "Failed to detect zero-obstacle path in example 2"

def test_single_cell():
    grid = [[0]]
    assert minimumObstacles(grid) == 0, "Failed for single-cell grid"

def test_2x2_minimal():
    grid = [[0,1], [1,0]]
    assert minimumObstacles(grid) == 1, "Failed to find minimal path in 2x2 grid"

def test_alternative_paths():
    grid = [
        [0, 0, 1],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert minimumObstacles(grid) == 1, "Failed to select optimal path with alternative routes"