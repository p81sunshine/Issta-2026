from solution import *

def test_example_1():
    assert self_dividing_numbers(1, 22) == [1,2,3,4,5,6,7,8,9,11,12,15,22], "Should include 22 in the output"

def test_example_2():
    assert self_dividing_numbers(47, 85) == [48,55,66,77], "Should return correct self-dividing numbers"

def test_edge_case_single_valid():
    assert self_dividing_numbers(22, 22) == [22], "Should return [22] when left=right=22"

def test_edge_case_single_invalid():
    assert self_dividing_numbers(0, 0) == [], "Should return empty list for 0 (invalid self-dividing number)"