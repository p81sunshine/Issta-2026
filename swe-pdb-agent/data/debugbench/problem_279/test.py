from solution import *

def test_example_1():
    assert sumSubarrayMins([3,1,2,4]) == 17, "First example failed"

def test_example_2():
    assert sumSubarrayMins([11,81,94,43,3]) == 444, "Second example failed"

def test_single_element():
    assert sumSubarrayMins([5]) == 5, "Single element test failed"

def test_two_elements_desc():
    assert sumSubarrayMins([2,1]) == 4, "Descending two elements test failed"

def test_two_elements_asc():
    assert sumSubarrayMins([1,2]) == 4, "Ascending two elements test failed"