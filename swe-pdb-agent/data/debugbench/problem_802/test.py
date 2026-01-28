from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert findKthLargest(nums, k) == 5

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert findKthLargest(nums, k) == 4

def test_edge_case_k_equals_length():
    nums = [5,3,1]
    k = 3
    assert findKthLargest(nums, k) == 1

def test_case_small_list():
    nums = [2,1]
    k = 2
    assert findKthLargest(nums, k) == 1