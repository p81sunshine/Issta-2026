from solution import *

def test_example_1():
    nums = [9,12,5,10,14,3,10]
    pivot = 10
    expected = [9,5,3,10,10,12,14]
    actual = pivotArray(nums, pivot)
    assert actual == expected, "Example 1 failed"

def test_example_2():
    nums = [-3,4,3,2]
    pivot = 2
    expected = [-3,2,4,3]
    actual = pivotArray(nums, pivot)
    assert actual == expected, "Example 2 failed"

def test_edge_case():
    nums = [5]
    pivot = 3
    expected = [5]
    actual = pivotArray(nums, pivot)
    assert actual == expected, "Edge case failed"