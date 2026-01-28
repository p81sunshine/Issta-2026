from solution import *

def test_example_1():
    assert self_dividing_numbers(1, 22) == [1,2,3,4,5,6,7,8,9,11,12,15,22], "Example 1 failed"

def test_example_2():
    assert self_dividing_numbers(47, 85) == [48,55,66,77], "Example 2 failed"

def test_zero_in_number():
    assert self_dividing_numbers(10, 10) == [], "Test case with zero in digits failed"

def test_single_valid_number():
    assert self_dividing_numbers(2, 2) == [2], "Single valid number test failed"

def test_zero_range():
    assert self_dividing_numbers(0, 0) == [], "Test zero range failed"