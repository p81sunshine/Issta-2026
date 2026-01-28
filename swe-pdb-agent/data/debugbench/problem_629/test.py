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
    nums = [5,3,1]
    k = 1
    assert findKthLargest(nums, k) == 5, "k=1 case failed"

def test_k_equals_length():
    nums = [3,1,2]
    k = 3
    assert findKthLargest(nums, k) == 1, "k equals list length case failed"

def test_small_even_list():
    nums = [5,3,1,2]
    k = 3
    assert findKthLargest(nums, k) == 2, "Small even list case failed"