from solution import *

def test_example_1():
    assert plusOne([1,2,3]) == [1,2,4], "Example 1 failed"

def test_example_2():
    assert plusOne([4,3,2,1]) == [4,3,2,2], "Example 2 failed"

def test_example_3():
    assert plusOne([9]) == [1,0], "Example 3 failed"

def test_single_digit_increment():
    assert plusOne([1]) == [2], "Single-digit increment failed"

def test_edge_case_zeros():
    assert plusOne([0,0]) == [1], "Edge case with zeros failed"