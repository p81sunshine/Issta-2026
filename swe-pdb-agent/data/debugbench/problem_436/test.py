from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_s2_not_subset():
    assert get_max_repetitions("abc", 5, "abd", 1) == 0, "s2 contains invalid characters"

def test_n1_zero():
    assert get_max_repetitions("a", 0, "a", 1) == 0, "n1=0 should return 0"

def test_s2_longer_than_s1():
    assert get_max_repetitions("ab", 2, "aba", 1) == 1, "s2 longer than s1 but valid"