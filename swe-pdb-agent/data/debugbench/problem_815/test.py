from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_s2_not_subset():
    assert get_max_repetitions("abc", 5, "xyz", 1) == 0, "s2 not subset of s1 should return 0"

def test_n1_zero():
    assert get_max_repetitions("abc", 0, "a", 1) == 0, "n1=0 should return 0"

def test_incomplete_s2():
    assert get_max_repetitions("ab", 1, "aba", 1) == 0, "s2 cannot be formed even once"