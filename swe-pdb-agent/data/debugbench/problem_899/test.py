from solution import *

def test_example_1():
    assert getMaxRepetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert getMaxRepetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_return_condition_buggy():
    assert getMaxRepetitions("ab", 2, "ab", 1) == 2, "Buggy condition test failed"

def test_missing_characters():
    assert getMaxRepetitions("abc", 3, "abd", 1) == 0, "Missing characters test failed"

def test_zero_possible():
    assert getMaxRepetitions("a", 1, "ab", 1) == 0, "Zero possible repetitions test failed"