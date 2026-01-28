from solution import *

def test_example_1():
    assert number_of_arithmetic_slices([2,4,6,8,10]) == 7, "Failed on example 1"

def test_example_2():
    assert number_of_arithmetic_slices([7,7,7,7,7]) == 16, "Failed on example 2"

def test_edge_case_empty():
    assert number_of_arithmetic_slices([]) == 0, "Failed on empty input"

def test_edge_case_two_elements():
    assert number_of_arithmetic_slices([1,2]) == 0, "Failed on two elements"

def test_edge_case_minimal():
    assert number_of_arithmetic_slices([1,2,3]) == 1, "Failed on minimal valid case"