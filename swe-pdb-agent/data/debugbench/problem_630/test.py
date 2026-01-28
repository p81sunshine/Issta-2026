from solution import *

def test_example_1():
    assert findMedianSortedArrays([1, 3], [2]) == 2.0, "Failed for example 1"

def test_example_2():
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5, "Failed for example 2"

def test_edge_case_single_element():
    assert findMedianSortedArrays([2], []) == 2.0, "Failed for single-element array"

def test_mixed_arrays():
    assert findMedianSortedArrays([3, 4], [1, 2]) == 2.5, "Failed for mixed arrays"

def test_uneven_lengths():
    assert findMedianSortedArrays([1, 2, 3], [4]) == 2.5, "Failed for uneven lengths"