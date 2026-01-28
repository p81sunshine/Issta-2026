from solution import *

def test_example_1():
    assert minCost(7, [1,3,4,5]) == 16, "Example 1 should return 16"

def test_example_2():
    assert minCost(9, [5,6,1,4,2]) == 22, "Example 2 should return 22"

def test_no_cuts():
    assert minCost(5, []) == 0, "No cuts should return 0 cost"

def test_single_cut():
    assert minCost(2, [1]) == 2, "Single cut should return correct minimal cost"