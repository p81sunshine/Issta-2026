from solution import *

def test_example_1():
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    expected = [-1,3,-1]
    assert nextGreaterElement(nums1, nums2) == expected, "Failed for example 1"

def test_example_2():
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    expected = [3,-1]
    assert nextGreaterElement(nums1, nums2) == expected, "Failed for example 2"

def test_no_next_greater():
    nums1 = [5]
    nums2 = [5]
    expected = [-1]
    assert nextGreaterElement(nums1, nums2) == expected, "Failed for single element case"

def test_multiple_elements():
    nums1 = [3, 1]
    nums2 = [3, 1, 2]
    expected = [-1, 2]
    assert nextGreaterElement(nums1, nums2) == expected, "Failed for multiple elements scenario"