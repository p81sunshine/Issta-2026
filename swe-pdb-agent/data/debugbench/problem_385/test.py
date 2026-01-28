from solution import *

def test_example_1():
    assert minSteps("leetcode", "coats") == 7, "Example 1 failed"

def test_example_2():
    assert minSteps("night", "thing") == 0, "Example 2 failed"

def test_case_aab_abb():
    assert minSteps("aab", "abb") == 2, "Test case aab vs abb failed"

def test_case_aa_a():
    assert minSteps("aa", "a") == 1, "Test case aa vs a failed"