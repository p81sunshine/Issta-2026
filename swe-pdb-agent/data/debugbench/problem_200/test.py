from solution import *

def test_example_1():
    assert minCost(7, [1,3,4,5]) == 16, "First example should return 16"

def test_example_2():
    assert minCost(9, [5,6,1,4,2]) == 22, "Second example should return 22"

def test_no_cuts():
    assert minCost(2, []) == 0, "No cuts should result in zero cost"

def test_single_cut():
    assert minCost(2, [1]) == 2, "Single cut should cost 2"