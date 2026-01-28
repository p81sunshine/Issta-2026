from solution import *

def test_example_1():
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0, "Test case 1 failed"

def test_example_2():
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5, "Test case 2 failed"

def test_edge_case_single_elements():
    assert find_median_sorted_arrays([1], [2]) == 1.5, "Single element arrays failed"