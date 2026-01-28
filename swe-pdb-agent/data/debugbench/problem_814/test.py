from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_s2_not_subset():
    assert get_max_repetitions("abc", 5, "abd", 2) == 0, "s2 contains char not in s1"

def test_cycle_handling():
    assert get_max_repetitions("ab", 3, "ab", 1) == 3, "Cycle detection logic failed"