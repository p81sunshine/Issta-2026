from solution import *

def test_example_1():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5, "Should return 5 as the 2nd largest"

def test_example_2():
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4, "Should return 4 as the 4th largest"

def test_k_is_1():
    assert findKthLargest([5, 2, 7], 1) == 7, "Should return maximum element when k=1"

def test_k_equal_to_length():
    assert findKthLargest([3, 1, 2], 3) == 1, "Should return minimum element when k=len(nums)"

def test_all_duplicates():
    assert findKthLargest([2, 2, 2], 2) == 2, "Should handle all duplicate elements correctly"