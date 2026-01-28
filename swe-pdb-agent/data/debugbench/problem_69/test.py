from solution import *

def test_example_1():
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    expected = [-1,3,-1]
    actual = nextGreaterElement(nums1, nums2)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_2():
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    expected = [3,-1]
    actual = nextGreaterElement(nums1, nums2)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_single_element_case():
    nums1 = [1]
    nums2 = [1,2]
    expected = [2]
    actual = nextGreaterElement(nums1, nums2)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_next_greater_in_middle():
    nums1 = [3]
    nums2 = [1,2,3,4]
    expected = [4]
    actual = nextGreaterElement(nums1, nums2)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_multiple_elements_mixed():
    nums1 = [2,1]
    nums2 = [1,2,1]
    expected = [-1,2]
    actual = nextGreaterElement(nums1, nums2)
    assert actual == expected, f"Expected {expected} but got {actual}"