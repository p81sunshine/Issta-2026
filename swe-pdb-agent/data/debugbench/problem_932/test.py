from solution import *

def test_example_1():
    assert largestInteger(1234) == 3412, "Failed for input 1234"

def test_example_2():
    assert largestInteger(65875) == 87655, "Failed for input 65875"

def test_single_digit():
    assert largestInteger(5) == 5, "Failed for single digit input"

def test_all_even_digits():
    assert largestInteger(2468) == 8642, "Failed for all even digits input"

def test_zero():
    assert largestInteger(0) == 0, "Failed for zero input"