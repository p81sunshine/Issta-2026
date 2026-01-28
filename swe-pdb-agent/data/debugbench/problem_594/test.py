from solution import *

def test_example_1():
    assert getMaxRepetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert getMaxRepetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_no_subset():
    assert getMaxRepetitions("abc", 5, "abd", 1) == 0, "Subset check failed"

def test_n1_zero():
    assert getMaxRepetitions("a", 0, "a", 1) == 0, "n1=0 edge case failed"

def test_missing_char():
    assert getMaxRepetitions("b", 3, "ab", 1) == 0, "Missing char case failed"