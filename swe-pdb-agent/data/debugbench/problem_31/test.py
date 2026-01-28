from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert findKthLargest(nums, k) == 5, "Test case 1 failed"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert findKthLargest(nums, k) == 4, "Test case 2 failed"

def test_k_equal_length():
    nums = [5,4,3,2,1]
    k = 5
    assert findKthLargest(nums, k) == 1, "Test k equals list length failed"

def test_k_1():
    nums = [5,3,1]
    k = 1
    assert findKthLargest(nums, k) == 5, "Test k=1 failed"

def test_duplicates():
    nums = [2,2,3,1]
    k = 2
    assert findKthLargest(nums, k) == 2, "Test with duplicates failed"