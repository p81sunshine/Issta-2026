from solution import *

def test_example_1():
    assert waysToSplitArray([10,4,-8,7]) == 2, "Example 1 failed"

def test_example_2():
    assert waysToSplitArray([2,3,1,0]) == 2, "Example 2 failed"

def test_small_case():
    assert waysToSplitArray([5,3]) == 1, "Small case failed"

def test_all_valid_splits():
    assert waysToSplitArray([3,1,1]) == 2, "All valid splits case failed"