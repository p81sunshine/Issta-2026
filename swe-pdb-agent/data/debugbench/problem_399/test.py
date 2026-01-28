from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert findKthLargest(nums, k) == 5, "Example 1 failed"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert findKthLargest(nums, k) == 4, "Example 2 failed"

def test_k_equals_1():
    nums = [5,3,1,2,4]
    k = 1
    assert findKthLargest(nums, k) == 5, "Failed when k=1"

def test_k_medium():
    nums = [1,2,3,4]
    k = 3
    assert findKthLargest(nums, k) == 2, "Failed for medium k value"

def test_k_equals_length():
    nums = [5,1,3]
    k = 3
    assert findKthLargest(nums, k) == 1, "Failed when k equals array length"