from solution import *

def test_example_1():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5

def test_example_2():
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

def test_k_equals_1():
    assert findKthLargest([5], 1) == 5, "Should return maximum element when k=1"

def test_k_equals_len():
    assert findKthLargest([3,1,2], 3) == 1, "Should return minimum element when k=len(nums)"

def test_middle_element():
    assert findKthLargest([5,3,1,4], 3) == 3, "Should return correct middle-ranked element"