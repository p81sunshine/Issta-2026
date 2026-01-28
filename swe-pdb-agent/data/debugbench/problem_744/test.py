from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert findKthLargest(nums, k) == 5, "Example 1 failed: Expected 5 as the 2nd largest element"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert findKthLargest(nums, k) == 4, "Example 2 failed: Expected 4 as the 4th largest element"

def test_k_equals_1():
    nums = [3,2,1,5,6,4]
    k = 1
    assert findKthLargest(nums, k) == 6, "Failed for k=1: Should return the maximum element"

def test_all_elements_same():
    nums = [2,2,2]
    k = 2
    assert findKthLargest(nums, k) == 2, "Failed for all identical elements: Should return the same value"

def test_k_equals_length():
    nums = [5,3,1,4]
    k = 4
    assert findKthLargest(nums, k) == 1, "Failed for k equals list length: Should return the smallest element"