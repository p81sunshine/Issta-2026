from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0, "Example 1 failed"

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5, "Example 2 failed"

def test_one_array_empty():
    assert findMedianSortedArrays([], [1,2,3]) == 2.0, "Empty nums1 failed"

def test_other_array_empty():
    assert findMedianSortedArrays([5], []) == 5.0, "Empty nums2 failed"

def test_even_length_with_empty():
    assert findMedianSortedArrays([], [1,2]) == 1.5, "Even-length nums2 with empty nums1 failed"