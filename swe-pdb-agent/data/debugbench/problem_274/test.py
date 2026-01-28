from solution import *

def test_example_1():
    assert findMedianSortedArrays([1, 3], [2]) == 2.0, "Failed for example 1"

def test_example_2():
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5, "Failed for example 2"

def test_edge_case_empty_nums1():
    assert findMedianSortedArrays([], [1]) == 1.0, "Failed for empty nums1"

def test_edge_case_empty_nums2():
    assert findMedianSortedArrays([1], []) == 1.0, "Failed for empty nums2"

def test_merged_longer_arrays():
    assert findMedianSortedArrays([1, 2, 3], [4, 5, 6]) == 3.5, "Failed for merged longer arrays"