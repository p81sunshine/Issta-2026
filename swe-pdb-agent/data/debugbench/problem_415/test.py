from solution import *

def test_example_1():
    assert find_median_sorted_arrays([1,3], [2]) == 2.0, "Example 1: merged [1,2,3] should return 2.0 as median"

def test_example_2():
    assert find_median_sorted_arrays([1,2], [3,4]) == 2.5, "Example 2: merged [1,2,3,4] should return 2.5 as median"

def test_one_empty_array():
    assert find_median_sorted_arrays([], [1]) == 1.0, "Edge case: nums1 is empty, nums2 has single element"

def test_unequal_lengths():
    assert find_median_sorted_arrays([4,5], [1,2,3]) == 3.0, "Unequal lengths: nums1 has smaller elements after nums2"

def test_all_equal_elements():
    assert find_median_sorted_arrays([0,0], [0,0]) == 0.0, "All elements equal: merged array [0,0,0,0] should return 0.0"