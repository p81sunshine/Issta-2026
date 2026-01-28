from solution import *

def test_example_1():
    assert number_of_arithmetic_slices([2,4,6,8,10]) == 7, "Example 1 failed"

def test_example_2():
    assert number_of_arithmetic_slices([7,7,7,7,7]) == 16, "Example 2 failed"

def test_edge_two_elements():
    assert number_of_arithmetic_slices([1, 2]) == 0, "Should return 0 for 2 elements"

def test_edge_empty():
    assert number_of_arithmetic_slices([]) == 0, "Should return 0 for empty list"

def test_small_case():
    assert number_of_arithmetic_slices([1,3,5,7]) == 3, "Test case [1,3,5,7] failed"