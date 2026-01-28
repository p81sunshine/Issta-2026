from solution import *

def test_example_1():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5

def test_example_2():
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

def test_single_element_list():
    assert findKthLargest([1], 1) == 1

def test_k_equals_array_length():
    assert findKthLargest([5,3,1], 3) == 1

def test_duplicate_values():
    assert findKthLargest([2,2,3,1], 2) == 2