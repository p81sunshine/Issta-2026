from solution import *

def test_example_1():
    assert findMedianSortedArrays([1, 3], [2]) == 2.0, "Failed for merged array [1,2,3]"

def test_example_2():
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5, "Failed for merged array [1,2,3,4]"

def test_empty_nums1():
    assert findMedianSortedArrays([], [1]) == 1.0, "Failed when nums1 is empty"

def test_empty_nums2():
    assert findMedianSortedArrays([5], []) == 5.0, "Failed when nums2 is empty"

def test_single_element_merged():
    assert findMedianSortedArrays([3], [1, 2]) == 2.0, "Failed for merged array [1,2,3] with reversed input order"

def test_nums2_longer():
    assert findMedianSortedArrays([1], [2, 3]) == 2.0, "Failed for out-of-bounds index in buggy code"