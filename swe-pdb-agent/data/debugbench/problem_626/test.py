from solution import *

def test_example_1():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5

def test_example_2():
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

def test_k_equals_one():
    assert findKthLargest([5,3,1,4,2], 1) == 5, "Should return maximum element when k=1"

def test_k_equals_length():
    assert findKthLargest([5,3,1,4,2], 5) == 1, "Should return minimum element when k=len(nums)"

def test_single_element():
    assert findKthLargest([7], 1) == 7, "Should return single element when k=1"