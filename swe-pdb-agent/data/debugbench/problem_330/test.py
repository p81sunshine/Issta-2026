from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert findKthLargest(nums, k) == 5, "Example 1 failed"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert findKthLargest(nums, k) == 4, "Example 2 failed"

def test_k_equals_length():
    nums = [5,3,1,4,2]
    k = 5
    assert findKthLargest(nums, k) == 1, "k equals list length failed"

def test_single_element():
    nums = [1]
    k = 1
    assert findKthLargest(nums, k) == 1, "Single element test failed"

def test_k_three_small_list():
    nums = [5,1,3]
    k = 3
    assert findKthLargest(nums, k) == 1, "Test for k=3 on small list failed"