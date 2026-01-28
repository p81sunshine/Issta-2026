from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_s2_not_subset():
    assert get_max_repetitions("abc", 3, "abd", 1) == 0, "s2 contains chars not in s1 failed"

def test_n1_zero():
    assert get_max_repetitions("a", 0, "a", 1) == 0, "n1=0 edge case failed"

def test_s2_exact_match():
    assert get_max_repetitions("ab", 1, "ab", 1) == 1, "s2 exactly matches s1 failed"