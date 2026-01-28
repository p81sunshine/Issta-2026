from solution import *

def test_example_1():
    assert sumSubarrayMins([3,1,2,4]) == 17, "Example 1 failed"

def test_example_2():
    assert sumSubarrayMins([11,81,94,43,3]) == 444, "Example 2 failed"

def test_decreasing_array():
    assert sumSubarrayMins([5,4,3,2,1]) == 35, "Test for strictly decreasing array failed"

def test_single_element():
    assert sumSubarrayMins([2]) == 2, "Test for single-element array failed"

def test_duplicate_elements():
    assert sumSubarrayMins([1,3,3]) == 12, "Test for array with duplicates failed"