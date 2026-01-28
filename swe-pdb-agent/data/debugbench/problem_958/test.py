from solution import *

def test_example_1():
    assert find_median_sorted_arrays([1,3], [2]) == 2.0, "Failed for example 1"

def test_example_2():
    assert find_median_sorted_arrays([1,2], [3,4]) == 2.5, "Failed for example 2"

def test_one_array_empty():
    assert find_median_sorted_arrays([], [1,2,3,4]) == 2.5, "Failed for one empty array"

def test_one_array_smaller():
    assert find_median_sorted_arrays([1,2], [3,4]) == 2.5, "Failed for one array smaller than the other"

def test_merged_odd_length():
    assert find_median_sorted_arrays([1,3,5], [2,4]) == 3.0, "Failed for merged odd-length array"