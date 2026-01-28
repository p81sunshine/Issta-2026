from solution import *

def test_example_1():
    actual = powerful_integers(2, 3, 10)
    expected = [2,3,4,5,7,9,10]
    assert sorted(actual) == sorted(expected), "Example 1 failed"

def test_example_2():
    actual = powerful_integers(3, 5, 15)
    expected = [2,4,6,8,10,14]
    assert sorted(actual) == sorted(expected), "Example 2 failed"

def test_bound_zero():
    actual = powerful_integers(1, 1, 0)
    expected = []
    assert actual == expected, "Bound zero case failed"

def test_x1_y1_bound2():
    actual = powerful_integers(1, 1, 2)
    expected = [2]
    assert sorted(actual) == sorted(expected), "x=1, y=1, bound=2 case failed"

def test_x1_y2_bound3():
    actual = powerful_integers(1, 2, 3)
    expected = [2,3]
    assert sorted(actual) == sorted(expected), "x=1, y=2, bound=3 case failed"