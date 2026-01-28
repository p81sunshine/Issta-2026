from solution import *

def test_example_1():
    assert getMinDistance([1,2,3,4,5], 5, 3) == 1, "Example 1 failed"

def test_example_2():
    assert getMinDistance([1], 1, 0) == 0, "Example 2 failed"

def test_example_3():
    assert getMinDistance([1]*10, 1, 0) == 0, "Example 3 failed"

def test_both_sides():
    assert getMinDistance([1,2,1], 1, 1) == 1, "Test case for elements on both sides failed"