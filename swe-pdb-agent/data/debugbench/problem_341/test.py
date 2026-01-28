from solution import *

def test_example_1():
    assert number_of_arithmetic_slices([2,4,6,8,10]) == 7, "Example 1 failed"

def test_example_2():
    assert number_of_arithmetic_slices([7,7,7,7,7]) == 16, "Example 2 failed"

def test_edge_case_2elements():
    assert number_of_arithmetic_slices([1,3]) == 0, "Edge case with 2 elements failed"

def test_edge_case_3elements():
    assert number_of_arithmetic_slices([1,3,5]) == 1, "Edge case with 3 elements failed"

def test_case_1_2_3_4():
    assert number_of_arithmetic_slices([1,2,3,4]) == 3, "Test case [1,2,3,4] failed"