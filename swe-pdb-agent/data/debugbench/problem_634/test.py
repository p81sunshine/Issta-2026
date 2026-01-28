from solution import *

def test_example_1():
    nums1 = [1, 3]
    nums2 = [2]
    expected = 2.0
    result = find_median_sorted_arrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_example_2():
    nums1 = [1, 2]
    nums2 = [3, 4]
    expected = 2.5
    result = find_median_sorted_arrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_edge_case_single_element():
    nums1 = [2]
    nums2 = [1]
    expected = 1.5
    result = find_median_sorted_arrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_empty_array():
    nums1 = []
    nums2 = [1, 2]
    expected = 1.5
    result = find_median_sorted_arrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_disjoint_arrays():
    nums1 = [1, 2, 3]
    nums2 = [5, 6, 7]
    expected = 4.0
    result = find_median_sorted_arrays(nums1, nums2)
    assert result == expected, f"Expected {expected}, but got {result}"