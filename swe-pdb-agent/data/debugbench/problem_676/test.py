from solution import *

def test_example_1():
    nums1 = [1, 3]
    nums2 = [2]
    assert findMedianSortedArrays(nums1, nums2) == 2.0, "Failed for example 1"

def test_example_2():
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert findMedianSortedArrays(nums1, nums2) == 2.5, "Failed for example 2"

def test_empty_nums1():
    nums1 = []
    nums2 = [1]
    assert findMedianSortedArrays(nums1, nums2) == 1.0, "Failed for empty nums1"

def test_empty_nums2():
    nums1 = [5]
    nums2 = []
    assert findMedianSortedArrays(nums1, nums2) == 5.0, "Failed for empty nums2"