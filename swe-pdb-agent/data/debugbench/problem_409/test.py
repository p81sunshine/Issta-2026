from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert findKthLargest(nums, k) == 5, "Failed for example 1"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert findKthLargest(nums, k) == 4, "Failed for example 2"

def test_k_equals_1():
    nums = [5,3,7]
    k = 1
    assert findKthLargest(nums, k) == 7, "Failed when k=1"

def test_k_equals_length():
    nums = [3,2,1]
    k = 3
    assert findKthLargest(nums, k) == 1, "Failed when k equals list length"

def test_regular_case():
    nums = [3,1,4]
    k = 2
    assert findKthLargest(nums, k) == 3, "Failed for regular case with duplicates"