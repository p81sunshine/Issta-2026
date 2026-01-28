from solution import *

def test_example_1():
    assert numberOfArithmeticSlices([2,4,6,8,10]) == 7, "Failed for example 1"

def test_example_2():
    assert numberOfArithmeticSlices([7,7,7,7,7]) == 16, "Failed for example 2"

def test_small_arithmetic_slice():
    assert numberOfArithmeticSlices([1,3,5]) == 1, "Failed for small arithmetic slice"

def test_multi_length_sequences():
    assert numberOfArithmeticSlices([1,2,3,4]) == 3, "Failed for multiple length sequences"

def test_edge_case_empty():
    assert numberOfArithmeticSlices([1]) == 0, "Failed for edge case with single element"
    assert numberOfArithmeticSlices([1,2]) == 0, "Failed for edge case with two elements"