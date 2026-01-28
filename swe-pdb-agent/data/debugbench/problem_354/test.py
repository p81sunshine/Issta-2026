from solution import *

def test_example_1():
    grid = [[1,2,4],[3,3,1]]
    assert deleteGreatestValue(grid) == 8

def test_example_2():
    grid = [[10]]
    assert deleteGreatestValue(grid) == 10

def test_2x2_case():
    grid = [[1,3],[4,2]]
    assert deleteGreatestValue(grid) == 6

def test_all_same_values():
    grid = [[5,5],[5,5]]
    assert deleteGreatestValue(grid) == 10

def test_3x3_case():
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    assert deleteGreatestValue(grid) == 24