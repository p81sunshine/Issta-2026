from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    expected = 5
    assert findKthLargest(nums, k) == expected, f"Expected {expected} but got {findKthLargest(nums, k)}"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    expected = 4
    assert findKthLargest(nums, k) == expected, f"Expected {expected} but got {findKthLargest(nums, k)}"

def test_single_element():
    nums = [1]
    k = 1
    expected = 1
    assert findKthLargest(nums, k) == expected, f"Expected {expected} but got {findKthLargest(nums, k)}"

def test_k_equals_length():
    nums = [5,3,1]
    k = 3
    expected = 1
    assert findKthLargest(nums, k) == expected, f"Expected {expected} but got {findKthLargest(nums, k)}"

def test_duplicates():
    nums = [2,2,3,3]
    k = 2
    expected = 3
    assert findKthLargest(nums, k) == expected, f"Expected {expected} but got {findKthLargest(nums, k)}"