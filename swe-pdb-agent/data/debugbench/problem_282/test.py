from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0, "Failed for [1,3] and [2]"

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5, "Failed for [1,2] and [3,4]"

def test_edge_empty_nums1():
    assert findMedianSortedArrays([], [1]) == 1.0, "Failed when nums1 is empty"

def test_edge_single_elements():
    assert findMedianSortedArrays([1], [2]) == 1.5, "Failed for single elements in both arrays"

def test_edge_even_merged():
    assert findMedianSortedArrays([0,0], [0,0]) == 0.0, "Failed for even-length merged array with all zeros"