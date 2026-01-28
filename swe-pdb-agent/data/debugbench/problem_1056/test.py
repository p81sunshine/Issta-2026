from solution import *

def test_example_1():
    grid = [[0,1,1],[1,1,0],[1,1,0]]
    assert minimum_obstacles(grid) == 2, "Test example 1 failed"

def test_example_2():
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    assert minimum_obstacles(grid) == 0, "Test example 2 failed"

def test_edge_case_1x1():
    grid = [[0]]
    assert minimum_obstacles(grid) == 0, "Test 1x1 grid failed"