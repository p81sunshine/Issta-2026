from solution import *

def test_example_1():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5

def test_example_2():
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

def test_k_equals_length():
    assert findKthLargest([5,3,1], 3) == 1

def test_k_1():
    assert findKthLargest([9,7,5], 1) == 9

def test_negative_numbers():
    assert findKthLargest([-1,-2,-3], 2) == -2