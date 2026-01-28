from solution import *

def test_example_1():
    nums1 = [1, 3]
    nums2 = [2]
    assert findMedianSortedArrays(nums1, nums2) == 2.0, "Failed for merged array [1,2,3]"

def test_example_2():
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert findMedianSortedArrays(nums1, nums2) == 2.5, "Failed for merged array [1,2,3,4]"

def test_empty_nums1():
    nums1 = []
    nums2 = [1]
    assert findMedianSortedArrays(nums1, nums2) == 1.0, "Failed when nums1 is empty"

def test_single_element_each():
    nums1 = [1]
    nums2 = [2]
    assert findMedianSortedArrays(nums1, nums2) == 1.5, "Failed for single-element arrays"

def test_nums2_longer():
    nums1 = [0, 1]
    nums2 = [2, 3, 4]
    assert findMedianSortedArrays(nums1, nums2) == 2.0, "Failed when nums2 is longer"