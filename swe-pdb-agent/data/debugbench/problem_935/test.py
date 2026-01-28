from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_not_subset_case():
    assert get_max_repetitions("abc", 5, "abd", 2) == 0, "Non-subset case failed"

def test_zero_n1():
    assert get_max_repetitions("abc", 0, "ab", 1) == 0, "Zero n1 case failed"

def test_cycle_calculation():
    assert get_max_repetitions("abab", 5, "ab", 1) == 10, "Cycle calculation case failed"