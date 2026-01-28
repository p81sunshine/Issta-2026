from solution import *

def test_example_1():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5

def test_example_2():
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

def test_edge_single_element():
    assert findKthLargest([10], 1) == 10, "Should return single element when k=1"

def test_edge_all_duplicates():
    assert findKthLargest([2,2,2,2], 2) == 2, "Should handle all duplicate values"

def test_edge_k_equals_length():
    nums = [5,3,1]
    k = len(nums)
    assert findKthLargest(nums, k) == 1, "Should return smallest element when k=len(nums)"