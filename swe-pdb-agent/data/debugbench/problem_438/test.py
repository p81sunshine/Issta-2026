from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert findKthLargest(nums, k) == 5, "Should return 5 as the 2nd largest element"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert findKthLargest(nums, k) == 4, "Should return 4 as the 4th largest element"

def test_k_equals_list_length():
    nums = [5, 3, 1, 2, 4]
    k = 5
    assert findKthLargest(nums, k) == 1, "Should return 1 as the 5th largest element in a list of 5 elements"

def test_all_elements_identical():
    nums = [2, 2, 2]
    k = 1
    assert findKthLargest(nums, k) == 2, "Should return 2 as the largest element when all elements are identical"