from solution import *

def test_example_1():
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    expected = [-1,3,-1]
    actual = nextGreaterElement(nums1, nums2)
    assert actual == expected, "Example 1 failed"

def test_example_2():
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    expected = [3,-1]
    actual = nextGreaterElement(nums1, nums2)
    assert actual == expected, "Example 2 failed"

def test_bug_case():
    nums1 = [4]
    nums2 = [1,4,3,2]
    expected = [-1]
    actual = nextGreaterElement(nums1, nums2)
    assert actual == expected, "Test case that triggers out-of-bounds in buggy code"

def test_edge_case_last_element():
    nums1 = [5]
    nums2 = [5]
    expected = [-1]
    actual = nextGreaterElement(nums1, nums2)
    assert actual == expected, "Edge case: single element in nums2"

def test_middle_element():
    nums1 = [1]
    nums2 = [2,1,3]
    expected = [3]
    actual = nextGreaterElement(nums1, nums2)
    assert actual == expected, "Test case for element in middle of nums2"