from solution import *

def test_example_1():
    assert minSteps("leetcode", "coats") == 7, "Example 1 failed"

def test_example_2():
    assert minSteps("night", "thing") == 0, "Example 2 failed"

def test_case_3():
    assert minSteps("aab", "abb") == 2, "Test case 3 failed"

def test_case_4():
    assert minSteps("aaa", "aa") == 1, "Test case 4 failed"