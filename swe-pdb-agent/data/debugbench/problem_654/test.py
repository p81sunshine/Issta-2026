from solution import *

def test_example_1():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5

def test_example_2():
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

def test_case_k_1():
    assert findKthLargest([5,3,1,4,2], 1) == 5

def test_case_k_equals_length():
    assert findKthLargest([5,3,1], 3) == 1

def test_case_all_duplicates():
    assert findKthLargest([2,2,2,2], 2) == 2

def test_case_single_element():
    assert findKthLargest([7], 1) == 7