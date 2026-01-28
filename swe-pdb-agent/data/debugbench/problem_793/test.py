from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    expected = 5
    assert findKthLargest(nums, k) == expected, "Example 1 failed"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    expected = 4
    assert findKthLargest(nums, k) == expected, "Example 2 failed"

def test_k_equals_length():
    nums = [5,3,1]
    k = 3
    expected = 1
    assert findKthLargest(nums, k) == expected, "Failed when k equals list length"

def test_medium_list_k3():
    nums = [1,3,5,2,4]
    k = 3
    expected = 3
    assert findKthLargest(nums, k) == expected, "Failed for medium list with k=3"

def test_k2_on_two_elements():
    nums = [2,1]
    k = 2
    expected = 1
    assert findKthLargest(nums, k) == expected, "Failed for two elements with k=2"