from solution import *

def test_example_1():
    assert getMaxRepetitions("acb", 4, "ab", 2) == 2

def test_example_2():
    assert getMaxRepetitions("acb", 1, "acb", 1) == 1

def test_s2_not_subset():
    assert getMaxRepetitions("abc", 5, "abd", 1) == 0

def test_s1_equals_s2():
    assert getMaxRepetitions("ab", 3, "ab", 1) == 3

def test_cycle_handling():
    assert getMaxRepetitions("ab", 2, "aba", 1) == 1