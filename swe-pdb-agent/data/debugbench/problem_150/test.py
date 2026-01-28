from solution import *

def test_example_1():
    actual = powerfulIntegers(2, 3, 10)
    expected = [2, 3, 4, 5, 7, 9, 10]
    assert sorted(actual) == sorted(expected), "Failed to include sum equal to bound"

def test_example_2():
    actual = powerfulIntegers(3, 5, 15)
    expected = [2, 4, 6, 8, 10, 14]
    assert sorted(actual) == sorted(expected), "Example 2 validation failed"

def test_sum_equal_bound():
    actual = powerfulIntegers(1, 1, 2)
    expected = [2]
    assert sorted(actual) == sorted(expected), "Failed to include exact bound value"

def test_bound_1():
    actual = powerfulIntegers(1, 1, 1)
    expected = []
    assert sorted(actual) == sorted(expected), "Edge case with bound=1 failed"

def test_x2_y1_bound3():
    actual = powerfulIntegers(2, 1, 3)
    expected = [2, 3]
    assert sorted(actual) == sorted(expected), "Failed to include sum equal to bound"