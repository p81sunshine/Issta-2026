from solution import *

def test_example_1():
    assert findMedianSortedArrays([1, 3], [2]) == 2.0, "Merged array [1,2,3] should have median 2.0"

def test_example_2():
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5, "Merged array [1,2,3,4] should have median 2.5"

def test_empty_nums1_odd_length():
    assert findMedianSortedArrays([], [5]) == 5.0, "Single-element array should return the element as median"

def test_empty_nums1_even_length():
    assert findMedianSortedArrays([], [1, 2]) == 1.5, "Two-element array should return average of elements"

def test_edge_case_infinite_loop():
    assert findMedianSortedArrays([], [1, 2, 3]) == 2.0, "Should handle appending remaining elements correctly"