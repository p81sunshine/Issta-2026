from solution import *

def test_example_1():
    actual = powerfulIntegers(2, 3, 10)
    expected = [2, 3, 4, 5, 7, 9, 10]
    assert sorted(actual) == sorted(expected), "Example 1 failed: 10 should be included"

def test_example_2():
    actual = powerfulIntegers(3, 5, 15)
    expected = [2, 4, 6, 8, 10, 14]
    assert sorted(actual) == sorted(expected), "Example 2 failed"

def test_edge_case_bound_zero():
    actual = powerfulIntegers(1, 1, 0)
    expected = []
    assert actual == expected, "Bound=0 should return empty list"

def test_edge_case_x_y_equal_1():
    actual = powerfulIntegers(1, 1, 2)
    expected = [2]
    assert sorted(actual) == sorted(expected), "1+1=2 should be included when bound=2"

def test_edge_case_sum_equals_bound():
    actual = powerfulIntegers(2, 1, 5)
    expected = [2, 3, 5]
    assert sorted(actual) == sorted(expected), "Sum equal to bound (5) should be included"