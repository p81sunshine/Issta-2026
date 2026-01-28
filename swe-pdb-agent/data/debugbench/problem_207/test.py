from solution import *

def test_example_1():
    grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
    assert minCost(grid) == 3, "Example 1 failed"

def test_example_2():
    grid = [[1,1,3],[3,2,2],[1,1,4]]
    assert minCost(grid) == 0, "Example 2 failed"

def test_example_3():
    grid = [[1,2],[4,3]]
    assert minCost(grid) == 1, "Example 3 failed"

def test_edge_single_cell():
    grid = [[5]]
    assert minCost(grid) == 0, "Single-cell grid failed"

def test_edge_1x2_grid():
    grid = [[1,1]]
    assert minCost(grid) == 0, "1x2 grid failed"