from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_subset_failure():
    assert get_max_repetitions("abc", 2, "abd", 1) == 0, "Subset check failed"

def test_cycle_handling():
    assert get_max_repetitions("ab", 5, "ab", 2) == 2, "Cycle calculation failed"

def test_n1_zero():
    assert get_max_repetitions("abc", 0, "ab", 1) == 0, "Zero n1 case failed"