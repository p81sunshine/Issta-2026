from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert findKthLargest(nums, k) == 5, "Should return 5 as the 2nd largest element"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert findKthLargest(nums, k) == 4, "Should return 4 as the 4th largest element"

def test_k_equals_1():
    nums = [5,3,1]
    k = 1
    assert findKthLargest(nums, k) == 5, "Should return maximum value when k=1"

def test_sorted_list():
    nums = [1,2,3,4,5]
    k = 3
    assert findKthLargest(nums, k) == 3, "Should return 3 as the 3rd largest in sorted list"

def test_all_elements_same():
    nums = [4,4,4]
    k = 2
    assert findKthLargest(nums, k) == 4, "Should return 4 when all elements are same"