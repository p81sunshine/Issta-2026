from solution import *

def test_example_1():
    actual = powerfulIntegers(2, 3, 10)
    expected = [2, 3, 4, 5, 7, 9, 10]
    assert sorted(actual) == sorted(expected), f"Failed for input (2, 3, 10). Expected {expected}, got {actual}"

def test_example_2():
    actual = powerfulIntegers(3, 5, 15)
    expected = [2, 4, 6, 8, 10, 14]
    assert sorted(actual) == sorted(expected), f"Failed for input (3, 5, 15). Expected {expected}, got {actual}"

def test_bound_zero():
    assert powerfulIntegers(1, 1, 0) == [], "Failed for bound=0 edge case"

def test_x_and_y_are_one():
    actual = powerfulIntegers(1, 1, 2)
    expected = [2]
    assert sorted(actual) == sorted(expected), f"Failed for x=1, y=1, bound=2. Expected {expected}, got {actual}"

def test_bound_one():
    assert powerfulIntegers(2, 3, 1) == [], "Failed for bound=1 edge case"