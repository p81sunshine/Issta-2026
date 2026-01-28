from solution import *

def test_example_1():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5, "Example 1 failed"

def test_example_2():
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4, "Example 2 failed"

def test_edge_case_k_equals_length():
    assert findKthLargest([3,1,2], 3) == 1, "Edge case where k equals list length failed"

def test_another_case():
    assert findKthLargest([4,3,2,1], 3) == 2, "Test case for len 4 and k=3 failed"

def test_k_equals_1():
    assert findKthLargest([5,3,1], 1) == 5, "Test case for k=1 failed"