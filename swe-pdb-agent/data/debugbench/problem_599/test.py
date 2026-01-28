from solution import *

def test_example_1():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5, "Example 1 failed"

def test_example_2():
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4, "Example 2 failed"

def test_k_equals_1():
    assert findKthLargest([5], 1) == 5, "Should return maximum element when k=1"

def test_k_equals_length():
    assert findKthLargest([1,2,3], 3) == 1, "Should return minimum element when k=len(nums)"

def test_duplicates():
    assert findKthLargest([3,3,3], 2) == 3, "Should handle arrays with all duplicates"