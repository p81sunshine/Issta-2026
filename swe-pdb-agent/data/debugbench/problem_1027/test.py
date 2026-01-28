from solution import *

def test_example_1():
    nums1 = [1, 3]
    nums2 = [2]
    assert findMedianSortedArrays(nums1, nums2) == 2.0, "Failed for example 1"

def test_example_2():
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert findMedianSortedArrays(nums1, nums2) == 2.5, "Failed for example 2"

def test_case_remaining_nums1():
    nums1 = [3, 4]
    nums2 = [1, 2]
    assert findMedianSortedArrays(nums1, nums2) == 2.5, "Failed when nums1 has remaining elements"

def test_case_duplicate_zeros():
    nums1 = [0, 0]
    nums2 = [0, 0]
    assert findMedianSortedArrays(nums1, nums2) == 0.0, "Failed for duplicate zeros case"

def test_edge_case_empty():
    nums1 = []
    nums2 = [1]
    assert findMedianSortedArrays(nums1, nums2) == 1.0, "Failed for empty nums1 case"