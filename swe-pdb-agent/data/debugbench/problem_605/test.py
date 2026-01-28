from solution import *

def test_example_1():
    assert getMaxRepetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert getMaxRepetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_subset_failure():
    assert getMaxRepetitions("abc", 5, "abd", 1) == 0, "Subset check failed"

def test_n1_zero():
    assert getMaxRepetitions("abc", 0, "ab", 1) == 0, "n1=0 case failed"

def test_cycle_case():
    assert getMaxRepetitions("ab", 5, "ab", 1) == 5, "Cycle calculation failed"