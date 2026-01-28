from solution import *

def test_example_1():
    nums1 = [1,3]
    nums2 = [2]
    expected = 2.0
    assert findMedianSortedArrays(nums1, nums2) == expected, "Failed for example 1"

def test_example_2():
    nums1 = [1,2]
    nums2 = [3,4]
    expected = 2.5
    assert findMedianSortedArrays(nums1, nums2) == expected, "Failed for example 2"

def test_empty_nums1():
    nums1 = []
    nums2 = [1]
    expected = 1.0
    assert findMedianSortedArrays(nums1, nums2) == expected, "Failed for empty nums1"

def test_all_zeros():
    nums1 = [0,0]
    nums2 = [0,0]
    expected = 0.0
    assert findMedianSortedArrays(nums1, nums2) == expected, "Failed for all zeros"