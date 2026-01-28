from solution import *

def test_example_1():
    assert findMiddleIndex([2,3,-1,8,4]) == 3, "Example 1 failed"

def test_example_2():
    assert findMiddleIndex([1,-1,4]) == 2, "Example 2 failed"

def test_example_3():
    assert findMiddleIndex([2,5]) == -1, "Example 3 failed"

def test_single_element():
    assert findMiddleIndex([0]) == 0, "Single element test failed"

def test_negative_numbers():
    assert findMiddleIndex([-1,-1,-1,-1,-1]) == 2, "Negative numbers test failed"