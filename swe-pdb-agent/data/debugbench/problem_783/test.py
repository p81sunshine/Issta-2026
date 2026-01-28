from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0, "Example 1: merged array [1,2,3], median should be 2.0"

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5, "Example 2: merged array [1,2,3,4], median should be 2.5"

def test_single_element_nums1():
    assert findMedianSortedArrays([5], []) == 5.0, "Single element in nums1 should return that element as median"

def test_single_element_nums2():
    assert findMedianSortedArrays([], [7]) == 7.0, "Single element in nums2 should return that element as median"

def test_remaining_elements_in_nums1():
    assert findMedianSortedArrays([4,5,6], [1,2]) == 4.0, "Merged array [1,2,4,5,6], median should be 4.0"