from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0, "Example 1 should return 2.0"

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5, "Example 2 should return 2.5"

def test_longer_nums1():
    assert findMedianSortedArrays([1,2,3], [4,5]) == 3.0, "Merged array [1,2,3,4,5] should have median 3.0"

def test_longer_nums2():
    assert findMedianSortedArrays([1,2], [3,4,5,6]) == 3.5, "Merged array [1,2,3,4,5,6] should have median 3.5"

def test_empty_nums1():
    assert findMedianSortedArrays([], [1,2,3]) == 2.0, "Single array [1,2,3] should have median 2.0"