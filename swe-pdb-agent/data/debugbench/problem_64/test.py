from solution import *

def test_example_1():
    assert number_of_arithmetic_slices([2,4,6,8,10]) == 7, "Failed for example 1"

def test_example_2():
    assert number_of_arithmetic_slices([7,7,7,7,7]) == 16, "Failed for example 2"

def test_small_case():
    assert number_of_arithmetic_slices([1,2,3]) == 1, "Failed for small arithmetic sequence"

def test_less_than_three_elements():
    assert number_of_arithmetic_slices([1,2]) == 0, "Failed for 2 elements"
    assert number_of_arithmetic_slices([5, 10]) == 0, "Failed for another 2 elements"
    assert number_of_arithmetic_slices([1]) == 0, "Failed for single element"

def test_additional_case():
    assert number_of_arithmetic_slices([1,2,3,4]) == 3, "Failed for extended arithmetic sequence"