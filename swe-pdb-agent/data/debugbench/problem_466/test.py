from solution import *

def test_example_1():
    assert getMaxRepetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert getMaxRepetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_cycle_case():
    assert getMaxRepetitions("ab", 2, "ab", 1) == 2, "Cycle calculation bug test failed"

def test_no_common_chars():
    assert getMaxRepetitions("abc", 3, "def", 1) == 0, "No overlapping chars test failed"

def test_n1_zero():
    assert getMaxRepetitions("abc", 0, "ab", 1) == 0, "Zero n1 edge case failed"