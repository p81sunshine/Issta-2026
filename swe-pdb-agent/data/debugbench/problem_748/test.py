from solution import *

def test_example_1():
    nums1 = [1, 3]
    nums2 = [2]
    assert findMedianSortedArrays(nums1, nums2) == 2.0, "Failed for case with odd merged length"

def test_example_2():
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert findMedianSortedArrays(nums1, nums2) == 2.5, "Failed for case with even merged length"

def test_one_empty():
    nums1 = []
    nums2 = [1]
    assert findMedianSortedArrays(nums1, nums2) == 1.0, "Failed for single-element array case"

def test_incorrect_pointer_increment():
    nums1 = [3]
    nums2 = [1, 2]
    assert findMedianSortedArrays(nums1, nums2) == 2.0, "Failed to handle second loop pointer increment bug"

def test_infinite_loop_edge_case():
    nums1 = [1]
    nums2 = [2, 3]
    assert findMedianSortedArrays(nums1, nums2) == 2.0, "Failed to handle third loop pointer increment bug"