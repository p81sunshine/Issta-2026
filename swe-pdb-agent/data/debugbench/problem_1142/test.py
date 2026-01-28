from solution import *

def test_example_1():
    assert largestInteger(1234) == 3412, "Failed for input 1234"

def test_example_2():
    assert largestInteger(65875) == 87655, "Failed for input 65875"

def test_edge_case_short_number():
    assert largestInteger(111) == 111, "Failed for all-odd digits"

def test_edge_case_zero():
    assert largestInteger(0) == 0, "Failed for zero input"

def test_edge_case_max_heap():
    assert largestInteger(13579) == 97531, "Failed for descending rearrangement"