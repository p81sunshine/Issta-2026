from solution import *

def test_example_1():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5, "Example 1 failed"

def test_example_2():
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4, "Example 2 failed"

def test_k_equals_1():
    assert findKthLargest([5,3,1], 1) == 5, "Test k=1 failed"

def test_duplicates_case():
    assert findKthLargest([1,2,3,3,4], 2) == 3, "Duplicates case failed"

def test_reverse_sorted():
    assert findKthLargest([5,4,3,2,1], 3) == 3, "Reverse sorted list failed"