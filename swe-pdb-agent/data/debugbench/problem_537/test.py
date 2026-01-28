from solution import *

def test_example_1():
    assert self_dividing_numbers(1, 22) == [1,2,3,4,5,6,7,8,9,11,12,15,22], "Failed for input 1-22"

def test_example_2():
    assert self_dividing_numbers(47, 85) == [48,55,66,77], "Failed for input 47-85"

def test_single_valid_number():
    assert self_dividing_numbers(2, 2) == [2], "Failed for single valid number"

def test_no_valid_numbers():
    assert self_dividing_numbers(10, 10) == [], "Failed for no valid numbers"