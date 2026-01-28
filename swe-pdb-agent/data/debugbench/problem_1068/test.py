from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0, "Failed for merged array [1,2,3]"

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5, "Failed for merged array [1,2,3,4]"

def test_edge_case_empty():
    assert findMedianSortedArrays([], [1]) == 1.0, "Failed for single-element array"

def test_edge_case_single_element():
    assert findMedianSortedArrays([5], [3]) == 4.0, "Failed for merged array [3,5]"

def test_case_remaining_elements():
    assert findMedianSortedArrays([3], [1,2]) == 2.0, "Failed for merged array [1,2,3]"