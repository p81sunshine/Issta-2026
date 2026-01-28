from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0, "Failed for example 1"

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5, "Failed for example 2"

def test_empty_nums1():
    assert findMedianSortedArrays([], [1]) == 1.0, "Failed when nums1 is empty"

def test_empty_nums2():
    assert findMedianSortedArrays([2], []) == 2.0, "Failed when nums2 is empty"

def test_all_zeros():
    assert findMedianSortedArrays([0,0], [0,0]) == 0.0, "Failed for all-zero inputs"