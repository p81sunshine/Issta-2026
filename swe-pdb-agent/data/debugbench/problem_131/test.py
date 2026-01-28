from solution import *

def test_example_1():
    grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
    assert minCost(grid) == 3, "Example 1 should return 3"

def test_example_2():
    grid = [[1,1,3],[3,2,2],[1,1,4]]
    assert minCost(grid) == 0, "Example 2 should return 0"

def test_example_3():
    grid = [[1,2],[4,3]]
    assert minCost(grid) == 1, "Example 3 should return 1"

def test_single_cell():
    grid = [[1]]
    assert minCost(grid) == 0, "Single cell grid should return 0"