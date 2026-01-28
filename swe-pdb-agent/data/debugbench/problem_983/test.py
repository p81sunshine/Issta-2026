from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    expected = 5
    actual = findKthLargest(nums, k)
    assert actual == expected, "Test example 1 failed"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    expected = 4
    actual = findKthLargest(nums, k)
    assert actual == expected, "Test example 2 failed"

def test_k_equals_1():
    nums = [5,3,1,4,2]
    k = 1
    expected = 5
    actual = findKthLargest(nums, k)
    assert actual == expected, "Test k=1 failed"

def test_edge_case_k_equals_length():
    nums = [3,1,4]
    k = 3
    expected = 1
    actual = findKthLargest(nums, k)
    assert actual == expected, "Test k equals length of nums failed"