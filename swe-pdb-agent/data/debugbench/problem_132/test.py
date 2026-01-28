from solution import *

def test_example_1():
    grid = [[2,5,4],[1,5,1]]
    assert gridGame(grid) == 4, "Failed for example 1"

def test_example_2():
    grid = [[3,3,1],[8,5,2]]
    assert gridGame(grid) == 4, "Failed for example 2"

def test_example_3():
    grid = [[1,3,1,15],[1,3,3,1]]
    assert gridGame(grid) == 7, "Failed for example 3"

def test_edge_case_single_column():
    grid = [[5],[2]]
    assert gridGame(grid) == 0, "Failed for single-column edge case"