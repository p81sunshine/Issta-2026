from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0, "Failed for merged array [1,2,3]"

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5, "Failed for merged array [1,2,3,4]"

def test_empty_nums1():
    assert findMedianSortedArrays([], [1]) == 1.0, "Failed when nums1 is empty"

def test_equal_elements():
    assert findMedianSortedArrays([1], [1]) == 1.0, "Failed for equal elements"

def test_merged_after_one_loop():
    assert findMedianSortedArrays([1,2], [3]) == 2.0, "Failed when merging after first loop"