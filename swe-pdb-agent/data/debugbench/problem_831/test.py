from solution import *

def test_example_1():
    nums1 = [1, 3]
    nums2 = [2]
    expected = 2.0
    result = findMedianSortedArrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, got {result}"

def test_example_2():
    nums1 = [1, 2]
    nums2 = [3, 4]
    expected = 2.5
    result = findMedianSortedArrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, got {result}"

def test_one_array_empty():
    nums1 = []
    nums2 = [1]
    expected = 1.0
    result = findMedianSortedArrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, got {result}"

def test_other_array_empty():
    nums1 = [1]
    nums2 = []
    expected = 1.0
    result = findMedianSortedArrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, got {result}"

def test_merged_odd_length():
    nums1 = [1, 2, 3]
    nums2 = [4, 5]
    expected = 3.0
    result = findMedianSortedArrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, got {result}"