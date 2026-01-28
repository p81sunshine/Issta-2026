from solution import *

def test_example_1():
    assert findMedianSortedArrays([1,3], [2]) == 2.0, "Example 1 failed"

def test_example_2():
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5, "Example 2 failed"

def test_mixed_arrays():
    assert findMedianSortedArrays([1,3,5], [2,4]) == 3.0, "Mixed arrays test failed"

def test_empty_nums1():
    assert findMedianSortedArrays([], [1]) == 1.0, "Empty nums1 test failed"

def test_all_zeros():
    assert findMedianSortedArrays([0,0], [0,0]) == 0.0, "All zeros test failed"