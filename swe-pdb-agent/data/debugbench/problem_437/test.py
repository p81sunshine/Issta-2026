from solution import *

def test_example_1():
    assert getMaxRepetitions("acb", 4, "ab", 2) == 2, "Example 1 should return 2"

def test_example_2():
    assert getMaxRepetitions("acb", 1, "acb", 1) == 1, "Example 2 should return 1"

def test_s2_not_subset():
    assert getMaxRepetitions("abc", 3, "abd", 1) == 0, "s2 contains 'd' not in s1 should return 0"

def test_cycle_condition_bug():
    assert getMaxRepetitions("ab", 2, "ab", 1) == 2, "Buggy code returns 1, correct code returns 2"