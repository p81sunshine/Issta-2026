from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0, "Failed for example 1"

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5, "Failed for example 2"

def test_case_empty_nums1():
    assert findMedianSortedArrays([], [1,2,3]) == 2.0, "Failed when nums1 is empty"

def test_case_uneven_lengths():
    assert findMedianSortedArrays([1,2,5], [3,4]) == 3.0, "Failed for uneven array lengths"