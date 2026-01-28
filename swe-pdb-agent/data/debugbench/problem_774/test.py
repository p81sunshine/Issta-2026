from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0, "Example 1 failed"

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5, "Example 2 failed"

def test_case_3():
    assert findMedianSortedArrays([3], [1,2]) == 2.0, "Test case with single-element nums1"

def test_edge_case_empty_nums1():
    assert findMedianSortedArrays([], [1,2,3]) == 2.0, "Edge case: nums1 is empty"

def test_edge_case_empty_nums2():
    assert findMedianSortedArrays([1,2,3], []) == 2.0, "Edge case: nums2 is empty"