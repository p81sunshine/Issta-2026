from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_s2_not_subset():
    assert get_max_repetitions("abc", 3, "abd", 1) == 0, "s2 not subset of s1 should return 0"

def test_n1_zero():
    assert get_max_repetitions("a", 0, "a", 1) == 0, "n1=0 should return 0"

def test_direct_mapping():
    assert get_max_repetitions("ab", 5, "ab", 1) == 5, "Direct 1:1 mapping case failed"

def test_insufficient_chars():
    assert get_max_repetitions("a", 3, "aa", 1) == 1, "Insufficient characters in s1 to form more s2"