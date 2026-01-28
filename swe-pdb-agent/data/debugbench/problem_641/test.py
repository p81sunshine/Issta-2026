from solution import *

def test_example_1():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5

def test_example_2():
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

def test_edge_case_k1():
    assert findKthLargest([5,3,1], 1) == 5

def test_edge_case_k_equal_length():
    assert findKthLargest([5], 1) == 5

def test_kth_vs_buggy_index():
    assert findKthLargest([4,3,2,1], 3) == 2