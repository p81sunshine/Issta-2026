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

def test_merged_odd_length():
    nums1 = [1, 2, 3]
    nums2 = [4, 5]
    assert findMedianSortedArrays(nums1, nums2) == 3.0, "Failed for merged array [1,2,3,4,5]"

def test_even_with_duplicates():
    nums1 = [1, 2]
    nums2 = [3, 3]
    assert findMedianSortedArrays(nums1, nums2) == 2.5, "Failed for merged array [1,2,3,3]"