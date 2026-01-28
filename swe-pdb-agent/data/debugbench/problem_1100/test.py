from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    expected = 5
    actual = findKthLargest(nums, k)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    expected = 4
    actual = findKthLargest(nums, k)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_k_equals_length():
    nums = [3,1,2]
    k = 3
    expected = 1
    actual = findKthLargest(nums, k)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_k_1():
    nums = [5,3,1]
    k = 1
    expected = 5
    actual = findKthLargest(nums, k)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_duplicate_values():
    nums = [2,2,3,1,1]
    k = 2
    expected = 2
    actual = findKthLargest(nums, k)
    assert actual == expected, f"Expected {expected}, got {actual}"