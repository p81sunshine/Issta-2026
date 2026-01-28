from solution import *

def test_example_1():
    assert sumSubarrayMins([3,1,2,4]) == 17, "Example 1 failed"

def test_example_2():
    assert sumSubarrayMins([11,81,94,43,3]) == 444, "Example 2 failed"

def test_single_element():
    assert sumSubarrayMins([5]) == 5, "Single element test failed"

def test_all_same_elements():
    assert sumSubarrayMins([2,2,2]) == 12, "All same elements test failed"

def test_increasing_array():
    assert sumSubarrayMins([1,2,3,4]) == 20, "Increasing array test failed"