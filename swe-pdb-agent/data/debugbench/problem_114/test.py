from solution import *

def test_example_1():
    assert third_max([3,2,1]) == 1, "Example 1 failed: should return third distinct maximum"

def test_example_2():
    assert third_max([1,2]) == 2, "Example 2 failed: should return maximum when less than 3 unique values"

def test_example_3():
    assert third_max([2,2,3,1]) == 1, "Example 3 failed: should handle duplicate values correctly"

def test_single_element():
    assert third_max([5,5,5]) == 5, "Single unique element case failed"

def test_four_unique_elements():
    assert third_max([4,3,2,1]) == 2, "Fourth unique element case failed"