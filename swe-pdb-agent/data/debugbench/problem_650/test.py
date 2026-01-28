from solution import *

def test_example_1():
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0, "Failed on example 1"

def test_example_2():
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5, "Failed on example 2"

def test_empty_array_1():
    assert find_median_sorted_arrays([], [1]) == 1.0, "Failed on empty array 1"

def test_empty_array_2():
    assert find_median_sorted_arrays([], [1, 2]) == 1.5, "Failed on empty array 2"

def test_merging_order():
    assert find_median_sorted_arrays([1], [2, 3]) == 2.0, "Failed on merging order"