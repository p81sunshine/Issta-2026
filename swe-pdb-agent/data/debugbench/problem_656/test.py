from solution import *

def test_example_1():
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    expected = [-1,3,-1]
    result = nextGreaterElement(nums1, nums2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_example_2():
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    expected = [3,-1]
    result = nextGreaterElement(nums1, nums2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_no_next_greater():
    nums1 = [2]
    nums2 = [1,2]
    expected = [-1]
    result = nextGreaterElement(nums1, nums2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_mixed_case():
    nums1 = [2,5]
    nums2 = [1,3,2,4,5]
    expected = [4, -1]
    result = nextGreaterElement(nums1, nums2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_element_at_end():
    nums1 = [5]
    nums2 = [1,2,5]
    expected = [-1]
    result = nextGreaterElement(nums1, nums2)
    assert result == expected, f"Expected {expected}, but got {result}"