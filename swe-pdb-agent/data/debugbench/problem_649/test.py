from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert findKthLargest(nums, k) == 5, "Expected 5 but got different value"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert findKthLargest(nums, k) == 4, "Expected 4 but got different value"

def test_k_is_1():
    nums = [5,3,1]
    k = 1
    assert findKthLargest(nums, k) == 5, "Failed when k=1"

def test_k_equals_length():
    nums = [5,3,1]
    k = 3
    assert findKthLargest(nums, k) == 1, "Failed when k equals list length"

def test_duplicate_values():
    nums = [2,1,2]
    k = 2
    assert findKthLargest(nums, k) == 2, "Failed with duplicate values"