from solution import *

def test_example_1():
    assert number_of_arithmetic_slices([2,4,6,8,10]) == 7, "Failed for example 1"

def test_example_2():
    assert number_of_arithmetic_slices([7,7,7,7,7]) == 16, "Failed for example 2"

def test_minimal_valid_case():
    assert number_of_arithmetic_slices([1,2,3]) == 1, "Failed for minimal valid case"

def test_insufficient_length():
    assert number_of_arithmetic_slices([1,2]) == 0, "Failed for insufficient length case"

def test_no_arithmetic_slices():
    assert number_of_arithmetic_slices([1,2,4,5]) == 0, "Failed for no arithmetic slices case"