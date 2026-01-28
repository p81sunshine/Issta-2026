from solution import *

def test_example_1():
    assert pivotArray([9,12,5,10,14,3,10], 10) == [9,5,3,10,10,12,14], "Example 1 failed"

def test_example_2():
    assert pivotArray([-3,4,3,2], 2) == [-3,2,4,3], "Example 2 failed"

def test_large_elements():
    assert pivotArray([10, 20], 10) == [10, 20], "Test with elements larger than list length failed"

def test_small_list():
    assert pivotArray([3, 1, 2], 2) == [1, 2, 3], "Test with small list failed"

def test_single_element():
    assert pivotArray([5], 5) == [5], "Test with single element failed"