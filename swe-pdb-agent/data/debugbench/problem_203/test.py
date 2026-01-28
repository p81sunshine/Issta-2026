from solution import *

def test_example_1():
    grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
    assert maxMoves(grid) == 3, "Example 1 failed"

def test_example_2():
    grid = [[3,2,4],[2,1,9],[1,1,7]]
    assert maxMoves(grid) == 0, "Example 2 failed"

def test_non_square_case():
    grid = [[1,2,3], [4,5,6]]
    assert maxMoves(grid) == 2, "Non-square grid test failed"

def test_single_row():
    grid = [[1,2,3,4]]
    assert maxMoves(grid) == 3, "Single row test failed"