from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    expected = 5
    assert findKthLargest(nums, k) == expected, "Should return 5 for [3,2,1,5,6,4], k=2"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    expected = 4
    assert findKthLargest(nums, k) == expected, "Should return 4 for [3,2,3,1,2,4,5,5,6], k=4"

def test_k_equals_one():
    nums = [5, 3, 1]
    k = 1
    expected = 5
    assert findKthLargest(nums, k) == expected, "Should return maximum element when k=1"

def test_all_elements_same():
    nums = [2, 2, 2]
    k = 2
    expected = 2
    assert findKthLargest(nums, k) == expected, "Should return element value when all elements are same"

def test_k_equals_length():
    nums = [5, 3, 1]
    k = 3
    expected = 1
    assert findKthLargest(nums, k) == expected, "Should return smallest element when k equals array length"