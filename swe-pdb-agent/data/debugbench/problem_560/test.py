from solution import *

def test_example_1():
    assert findMiddleIndex([2,3,-1,8,4]) == 3, "Example 1 failed"

def test_example_2():
    assert findMiddleIndex([1,-1,4]) == 2, "Example 2 failed"

def test_example_3():
    assert findMiddleIndex([2,5]) == -1, "Example 3 failed"

def test_single_element():
    assert findMiddleIndex([0]) == 0, "Single element array failed"

def test_leetcode_style_case():
    assert findMiddleIndex([1,7,3,6,5,6]) == 3, "LeetCode-style example failed"