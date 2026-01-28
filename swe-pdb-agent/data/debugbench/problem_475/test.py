from solution import *

def test_example_1():
    actual = self_dividing_numbers(1, 22)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_2():
    actual = self_dividing_numbers(47, 85)
    expected = [48, 55, 66, 77]
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_inclusive_right():
    actual = self_dividing_numbers(22, 22)
    expected = [22]
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_self_dividing_12():
    actual = self_dividing_numbers(12, 12)
    expected = [12]
    assert actual == expected, f"Expected {expected} but got {actual}"