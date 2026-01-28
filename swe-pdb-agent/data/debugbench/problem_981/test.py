from solution import *

def test_example_1():
    assert sumSubarrayMins([3,1,2,4]) == 17, "Example 1 failed"

def test_example_2():
    assert sumSubarrayMins([11,81,94,43,3]) == 444, "Example 2 failed"

def test_single_element_array():
    assert sumSubarrayMins([5]) == 5, "Single element test failed"

def test_all_elements_same():
    assert sumSubarrayMins([2,2,2]) == 12, "All elements same test failed"

def test_middle_minimum_case():
    assert sumSubarrayMins([3,1,3]) == 10, "Middle minimum test failed"