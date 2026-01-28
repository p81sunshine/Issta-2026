from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0, "Example 1 failed"

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5, "Example 2 failed"

def test_empty_nums1():
    assert findMedianSortedArrays([], [1]) == 1.0, "Test empty nums1 failed"

def test_merged_odd_length():
    assert findMedianSortedArrays([1,2], [3,4,5]) == 3.0, "Test merged odd length failed"

def test_nums1_shorter():
    assert findMedianSortedArrays([5], [1,2]) == 2.0, "Test nums1 shorter failed"