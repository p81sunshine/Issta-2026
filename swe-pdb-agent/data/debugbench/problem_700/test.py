from solution import *

def test_example_1():
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0

def test_example_2():
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5

def test_edge_empty_1():
    assert find_median_sorted_arrays([], [1]) == 1.0

def test_edge_overlapping():
    assert find_median_sorted_arrays([1, 4], [2, 3]) == 2.5

def test_single_element():
    assert find_median_sorted_arrays([5], [6]) == 5.5