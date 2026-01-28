from solution import *

def test_example_1():
    assert sumSubarrayMins([3,1,2,4]) == 17, "First example should return 17"

def test_example_2():
    assert sumSubarrayMins([11,81,94,43,3]) == 444, "Second example should return 444"

def test_single_element():
    assert sumSubarrayMins([5]) == 5, "Single element array should return the element itself"

def test_all_same_elements():
    assert sumSubarrayMins([2,2,2]) == 12, "All same elements should calculate 2*6 subarrays"