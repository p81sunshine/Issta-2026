from solution import *

def test_example_1():
    assert maxStrength([3, -1, -5, 2, 5, -9]) == 1350, "Example 1 failed"

def test_example_2():
    assert maxStrength([-4, -5, -4]) == 20, "Example 2 failed"

def test_single_element():
    assert maxStrength([5]) == 5, "Single element test failed"

def test_two_negatives():
    assert maxStrength([-3, -2]) == 6, "Two negatives test failed"

def test_zero_with_negatives():
    assert maxStrength([0, -1, -2]) == 2, "Zero with negatives test failed"

def test_zero_and_positive():
    assert maxStrength([0, -1, 2]) == 2, "Zero and positive test failed"