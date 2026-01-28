from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert findKthLargest(nums, k) == 5, "Test case 1 failed"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert findKthLargest(nums, k) == 4, "Test case 2 failed"

def test_case_k_1():
    nums = [5,3,7]
    k = 1
    assert findKthLargest(nums, k) == 7, "First largest element test failed"

def test_case_k_equals_length_minus_one():
    nums = [1,2,3,4,5]
    k = 3
    assert findKthLargest(nums, k) == 3, "k equals length minus one test failed"

def test_case_duplicates():
    nums = [5,3,5]
    k = 2
    assert findKthLargest(nums, k) == 5, "Duplicates handling test failed"