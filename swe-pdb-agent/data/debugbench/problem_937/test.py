from solution import *

def test_example_1():
    grid = [[2,5,4],[1,5,1]]
    expected = 4
    assert gridGame(grid) == expected, f"Expected {expected} for example 1, got {gridGame(grid)}"

def test_example_2():
    grid = [[3,3,1],[8,5,2]]
    expected = 4
    assert gridGame(grid) == expected, f"Expected {expected} for example 2, got {gridGame(grid)}"

def test_example_3():
    grid = [[1,3,1,15],[1,3,3,1]]
    expected = 7
    assert gridGame(grid) == expected, f"Expected {expected} for example 3, got {gridGame(grid)}"

def test_edge_case_two_columns():
    grid = [[1,2],[3,4]]
    expected = 2
    assert gridGame(grid) == expected, f"Edge case failed: Expected {expected}, got {gridGame(grid)}"