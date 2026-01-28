from solution import *

def test_example_1():
    assert numberOfGoodSubarraySplits([0,1,0,0,1]) == 3, "Example 1 failed"

def test_example_2():
    assert numberOfGoodSubarraySplits([0,1,0]) == 1, "Example 2 failed"

def test_no_ones():
    assert numberOfGoodSubarraySplits([0,0,0]) == 0, "Should return 0 when no 1s present"

def test_single_one():
    assert numberOfGoodSubarraySplits([1,0,0]) == 1, "Single 1 case should return 1"

def test_multiple_groups():
    assert numberOfGoodSubarraySplits([1,0,1,0,1]) == 4, "Multiple zero groups between 1s calculation failed"