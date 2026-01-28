from solution import *

def test_example_1():
    assert getMaxRepetitions("acb", 4, "ab", 2) == 2

def test_example_2():
    assert getMaxRepetitions("acb", 1, "acb", 1) == 1

def test_not_subset():
    assert getMaxRepetitions("abc", 3, "abd", 1) == 0

def test_cycle_case():
    assert getMaxRepetitions("ab", 4, "aba", 1) == 2

def test_ptr2_difference():
    assert getMaxRepetitions("ab", 5, "aba", 1) == 2