from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0, "Example 1 failed"

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5, "Example 2 failed"

def test_single_element_merge():
    assert findMedianSortedArrays([1], [2]) == 1.5, "Single element merge failed"

def test_empty_first_array():
    assert findMedianSortedArrays([], [1,2,3]) == 2.0, "Empty first array failed"

def test_empty_second_array():
    assert findMedianSortedArrays([5], []) == 5.0, "Empty second array failed"