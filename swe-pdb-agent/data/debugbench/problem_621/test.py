from solution import *

def test_example_1():
    assert getMaxRepetions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert getMaxRepetions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_subset_failure():
    assert getMaxRepetions("abc", 3, "abd", 1) == 0, "Subset check failed"

def test_n1_zero():
    assert getMaxRepetions("a", 0, "a", 1) == 0, "n1=0 case failed"

def test_cycle_case():
    assert getMaxRepetions("acb", 3, "ab", 2) == 1, "Cycle calculation failed"