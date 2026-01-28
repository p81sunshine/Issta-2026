from solution import *

def test_example_1():
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    assert minimumObstacles(grid) == 2, "Failed to calculate correct minimum obstacles for example 1"

def test_example_2():
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    assert minimumObstacles(grid) == 0, "Failed to calculate correct minimum obstacles for example 2"

def test_single_cell():
    grid = [[0]]
    assert minimumObstacles(grid) == 0, "Failed for single-cell grid"

def test_straight_path():
    grid = [[0,0,0], [0,0,0], [0,0,0]]
    assert minimumObstacles(grid) == 0, "Failed for unobstructed straight path"

def test_obstacle_required():
    grid = [[0,1], [1,0]]
    assert minimumObstacles(grid) == 1, "Failed to find minimum path through required obstacles"