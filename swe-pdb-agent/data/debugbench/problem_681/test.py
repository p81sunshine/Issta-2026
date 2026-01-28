from solution import *

def test_example_1():
    assert number_of_arithmetic_slices([2,4,6,8,10]) == 7, "Failed on example 1"

def test_example_2():
    assert number_of_arithmetic_slices([7,7,7,7,7]) == 16, "Failed on example 2"

def test_short_list():
    assert number_of_arithmetic_slices([1,3]) == 0, "Failed on short list"

def test_min_arithmetic():
    assert number_of_arithmetic_slices([1,2,3]) == 1, "Failed on minimal arithmetic sequence"

def test_longer_arithmetic():
    assert number_of_arithmetic_slices([1,2,3,4]) == 3, "Failed on longer arithmetic sequence"