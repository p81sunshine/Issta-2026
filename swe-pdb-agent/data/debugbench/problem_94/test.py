from solution import *

def test_example_1():
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    assert minimumObstacles(grid) == 2, "Failed on example 1"

def test_example_2():
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    assert minimumObstacles(grid) == 0, "Failed on example 2"

def test_single_cell():
    grid = [[1]]
    assert minimumObstacles(grid) == 0, "Failed on single cell grid"

def test_no_obstacles():
    grid = [[0,0], [0,0]]
    assert minimumObstacles(grid) == 0, "Failed on obstacle-free grid"

def test_path_choice():
    grid = [[0,1], [1,0]]
    assert minimumObstacles(grid) == 1, "Failed on path choice scenario"