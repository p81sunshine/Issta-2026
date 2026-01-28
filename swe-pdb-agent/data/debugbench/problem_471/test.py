from solution import *

def test_example_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert findKthLargest(nums, k) == 5, "Should return 5 as the 2nd largest in [3,2,1,5,6,4]"

def test_example_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert findKthLargest(nums, k) == 4, "Should return 4 as the 4th largest in [3,2,3,1,2,4,5,5,6]"

def test_edge_case_k_equals_length():
    nums = [5,4,3,2,1]
    k = 5
    assert findKthLargest(nums, k) == 1, "Should return 1 as the 5th largest in [5,4,3,2,1]"

def test_all_elements_same():
    nums = [2,2,2]
    k = 2
    assert findKthLargest(nums, k) == 2, "Should return 2 as the 2nd largest in [2,2,2]"