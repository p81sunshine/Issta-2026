from solution import *

def test_example_1():
    x, y, bound = 2, 3, 10
    expected = [2, 3, 4, 5, 7, 9, 10]
    actual = powerfulIntegers(x, y, bound)
    assert sorted(actual) == sorted(expected), "Failed for example 1"

def test_example_2():
    x, y, bound = 3, 5, 15
    expected = [2, 4, 6, 8, 10, 14]
    actual = powerfulIntegers(x, y, bound)
    assert sorted(actual) == sorted(expected), "Failed for example 2"

def test_sum_equals_bound():
    x, y, bound = 1, 1, 2
    expected = [2]
    actual = powerfulIntegers(x, y, bound)
    assert sorted(actual) == sorted(expected), "Failed when sum equals bound"

def test_bound_zero():
    x, y, bound = 2, 3, 0
    expected = []
    actual = powerfulIntegers(x, y, bound)
    assert actual == expected, "Failed for bound=0"

def test_x_is_1():
    x, y, bound = 1, 2, 3
    expected = [2, 3]
    actual = powerfulIntegers(x, y, bound)
    assert sorted(actual) == sorted(expected), "Failed when x=1"