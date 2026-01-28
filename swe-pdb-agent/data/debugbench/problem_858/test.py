from solution import *

def test_example_1():
    nums = [9,12,5,10,14,3,10]
    pivot = 10
    expected = [9,5,3,10,10,12,14]
    assert pivotArray(nums, pivot) == expected, "Example 1 failed"

def test_example_2():
    nums = [-3,4,3,2]
    pivot = 2
    expected = [-3,2,4,3]
    assert pivotArray(nums, pivot) == expected, "Example 2 failed"

def test_order_bug():
    nums = [0,1,2,3]
    pivot = 2
    expected = [0,1,2,3]
    assert pivotArray(nums, pivot) == expected, "Order bug test failed"

def test_edge_case_single_element():
    nums = [5]
    pivot = 5
    expected = [5]
    assert pivotArray(nums, pivot) == expected, "Single element test failed"

def test_edge_case_index_out_of_range():
    nums = [10]
    pivot = 10
    expected = [10]
    assert pivotArray(nums, pivot) == expected, "Index out of range test failed"