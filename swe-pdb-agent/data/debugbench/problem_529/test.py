from solution import *

def test_example_1():
    assert longestString(2, 5, 1) == 12, "Example 1 failed"

def test_example_2():
    assert longestString(3, 2, 2) == 14, "Example 2 failed"

def test_z_effect():
    assert longestString(1, 1, 1) == 6, "Z effect test failed"

def test_x_greater_than_y():
    assert longestString(5, 2, 3) == 16, "Test case where x > y failed"