from solution import *

def test_example_1():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5, "Should return 5 as the second largest element"

def test_example_2():
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4, "Should return 4 as the fourth largest element"

def test_edge_case_k1():
    assert findKthLargest([5,3,1], 1) == 5, "Should return the largest element when k=1"

def test_edge_case_k_equals_length():
    nums = [5, 3, 1]
    k = 3
    assert findKthLargest(nums, k) == 1, "Should return the smallest element when k equals array length"

def test_all_duplicates():
    assert findKthLargest([2,2,2], 2) == 2, "Should handle arrays with all duplicate values correctly"