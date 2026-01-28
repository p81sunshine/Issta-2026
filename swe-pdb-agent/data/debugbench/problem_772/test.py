from solution import *

def test_example_1():
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    assert minimumObstacles(grid) == 2, "Should return 2 for example 1"

def test_example_2():
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    assert minimumObstacles(grid) == 0, "Should return 0 for example 2"

def test_single_cell():
    grid = [[0]]
    assert minimumObstacles(grid) == 0, "Single cell grid should require 0 obstacles"

def test_path_with_alternative():
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    assert minimumObstacles(grid) == 0, "Should find a path with 0 obstacles"

def test_obstacle_required():
    grid = [
        [0, 1],
        [0, 1]
    ]
    assert minimumObstacles(grid) == 1, "Should require removing 1 obstacle"