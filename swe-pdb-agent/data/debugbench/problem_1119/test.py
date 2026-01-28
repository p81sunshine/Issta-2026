from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5

def test_empty_nums1():
    assert findMedianSortedArrays([], [1]) == 1.0

def test_empty_nums1_even():
    assert findMedianSortedArrays([], [1,2]) == 1.5

def test_case_mixed():
    assert findMedianSortedArrays([5], [1,2,3,4]) == 3.0