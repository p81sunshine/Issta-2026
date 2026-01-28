from solution import *

def test_example_1():
    assert findMedianSortedArrays([1, 3], [2]) == 2.0, "Failed for example 1"

def test_example_2():
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5, "Failed for example 2"

def test_empty_nums1():
    assert findMedianSortedArrays([], [1]) == 1.0, "Failed when nums1 is empty"

def test_nums2_longer():
    assert findMedianSortedArrays([1], [2, 3]) == 2.0, "Failed when nums2 is longer"

def test_nums1_longer():
    assert findMedianSortedArrays([3], [1, 2]) == 2.0, "Failed when nums1 is longer"