from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert findKthLargest(nums, k) == 5, "Example 1 should return 5 when k=2"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert findKthLargest(nums, k) == 4, "Example 2 should return 4 when k=4"

def test_edge_case_k_equals_length():
    nums = [1,2,3]
    k = 3
    assert findKthLargest(nums, k) == 1, "Should return smallest element when k equals list length"

def test_edge_case_large_k():
    nums = [1,2,3,4,5]
    k = 5
    assert findKthLargest(nums, k) == 1, "Should return 1 as the 5th largest in 5-element list"