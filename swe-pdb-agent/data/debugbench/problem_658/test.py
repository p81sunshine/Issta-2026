from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5

def test_one_empty_array():
    assert findMedianSortedArrays([], [1]) == 1.0

def test_other_empty_array():
    assert findMedianSortedArrays([7], []) == 7.0

def test_single_element_each():
    assert findMedianSortedArrays([1], [2]) == 1.5