from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_s2_not_subset():
    assert get_max_repetitions("abc", 3, "abd", 1) == 0, "s2 contains invalid characters"

def test_insufficient_repetitions():
    assert get_max_repetitions("ab", 1, "ab", 2) == 0, "Insufficient repetitions to meet n2"

def test_exact_repetitions():
    assert get_max_repetitions("ab", 2, "ab", 2) == 1, "Exact match with n1 and n2"