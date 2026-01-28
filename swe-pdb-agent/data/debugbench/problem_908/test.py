from solution import *

def test_example_1():
    assert findMedianSortedArrays([1, 3], [2]) == 2.0, "Example 1 failed"

def test_example_2():
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5, "Example 2 failed"

def test_empty_nums1():
    assert findMedianSortedArrays([], [1]) == 1.0, "Empty nums1 failed"

def test_empty_nums2():
    assert findMedianSortedArrays([1], []) == 1.0, "Empty nums2 failed"

def test_even_length():
    assert findMedianSortedArrays([0, 0], [0, 0]) == 0.0, "Even length test failed"