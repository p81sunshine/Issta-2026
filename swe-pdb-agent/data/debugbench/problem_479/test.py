from solution import *

def test_example_1():
    assert getLastMoment(4, [4,3], [0,1]) == 4, "Example 1 failed: incorrect time calculation for left and right ants"

def test_example_2():
    assert getLastMoment(7, [], [0,1,2,3,4,5,6,7]) == 7, "Example 2 failed: incorrect handling of empty left list"

def test_example_3():
    assert getLastMoment(7, [0,1,2,3,4,5,6,7], []) == 7, "Example 3 failed: incorrect handling of empty right list"

def test_right_array_min_bug():
    assert getLastMoment(3, [], [1,2]) == 2, "Test for right array min vs max bug: buggy code returns 1 instead of 2"