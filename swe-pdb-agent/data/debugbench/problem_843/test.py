from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    expected = 5
    assert findKthLargest(nums, k) == expected, "Example 1 failed"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    expected = 4
    assert findKthLargest(nums, k) == expected, "Example 2 failed"

def test_k_equals_1():
    nums = [5,3,1,2,4]
    k = 1
    expected = 5
    assert findKthLargest(nums, k) == expected, "Test k=1 failed"

def test_single_element():
    nums = [7]
    k = 1
    expected = 7
    assert findKthLargest(nums, k) == expected, "Single element test failed"

def test_k_equals_length():
    nums = [3,1,2]
    k = 3
    expected = 1
    assert findKthLargest(nums, k) == expected, "Test k equals length failed"