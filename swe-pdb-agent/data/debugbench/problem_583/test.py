from solution import *

def test_example_1():
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    assert minimum_obstacles(grid) == 2, "Test case 1 failed"

def test_example_2():
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    assert minimum_obstacles(grid) == 0, "Test case 2 failed"

def test_edge_case_1x1():
    grid = [[0]]
    assert minimum_obstacles(grid) == 0, "1x1 grid test failed"

def test_2x2_grid():
    grid = [[0,1], [1,0]]
    assert minimum_obstacles(grid) == 1, "2x2 grid test failed"

def test_straight_path():
    grid = [[0,0,0], [0,0,0]]
    assert minimum_obstacles(grid) == 0, "Straight path test failed"