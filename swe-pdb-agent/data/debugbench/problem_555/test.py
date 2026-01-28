from solution import *

def test_example_1():
    assert max_power([1,2,4,5,0], 1, 2) == 5, "Example 1 failed"

def test_example_2():
    assert max_power([4,4,4,4], 0, 3) == 4, "Example 2 failed"

def test_k_zero():
    assert max_power([3,1,5], 1, 0) == 4, "Failed when k=0"

def test_single_station():
    assert max_power([1], 0, 1) == 2, "Single station test failed"

def test_large_r():
    assert max_power([1,2], 1, 1) == 4, "Large r scenario failed"