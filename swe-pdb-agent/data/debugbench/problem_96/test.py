from solution import *

def test_example_1():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    expected = [-1, 3, -1]
    assert nextGreaterElement(nums1, nums2) == expected, "Example 1 failed"

def test_example_2():
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    expected = [3, -1]
    assert nextGreaterElement(nums1, nums2) == expected, "Example 2 failed"

def test_edge_single_element_with_next():
    nums1 = [2]
    nums2 = [1, 2, 3]
    expected = [3]
    assert nextGreaterElement(nums1, nums2) == expected, "Edge case with next element failed"

def test_edge_last_element_in_nums2():
    nums1 = [2]
    nums2 = [1, 2]
    expected = [-1]
    assert nextGreaterElement(nums1, nums2) == expected, "Edge case with last element in nums2 failed"

def test_empty_nums1():
    nums1 = []
    nums2 = [1, 2, 3]
    expected = []
    assert nextGreaterElement(nums1, nums2) == expected, "Empty nums1 case failed"