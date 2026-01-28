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

def test_empty_nums1():
    nums1 = []
    nums2 = [1]
    expected = 1.0
    result = findMedianSortedArrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, got {result}"

def test_empty_nums2():
    nums1 = [5]
    nums2 = []
    expected = 5.0
    result = findMedianSortedArrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, got {result}"

def test_merging_order():
    nums1 = [3]
    nums2 = [1, 2]
    expected = 2.0
    result = findMedianSortedArrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, got {result}"