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

def test_edge_case_k1_single_element():
    nums = [5]
    k = 1
    expected = 5
    assert findKthLargest(nums, k) == expected, "Edge case with single element and k=1 failed"

def test_edge_case_k_equals_length():
    nums = [5,3,1]
    k = 3
    expected = 1
    assert findKthLargest(nums, k) == expected, "Edge case where k equals list length failed"

def test_case_duplicate_values():
    nums = [2,2,3,1]
    k = 2
    expected = 2
    assert findKthLargest(nums, k) == expected, "Test case with duplicates failed"