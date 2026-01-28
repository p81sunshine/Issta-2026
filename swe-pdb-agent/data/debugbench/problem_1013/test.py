from solution import *

def test_example_1():
    assert sumSubarrayMins([3,1,2,4]) == 17, "First example failed"

def test_example_2():
    assert sumSubarrayMins([11,81,94,43,3]) == 444, "Second example failed"

def test_single_element():
    assert sumSubarrayMins([1]) == 1, "Single element test failed"

def test_decreasing_array():
    assert sumSubarrayMins([5,4,3,2,1]) == 35, "Decreasing array test failed"