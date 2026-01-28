from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_s2_not_subset():
    assert get_max_repetitions("abc", 5, "abd", 1) == 0, "s2 contains invalid characters"

def test_n1_zero():
    assert get_max_repetitions("a", 0, "a", 1) == 0, "n1=0 should return 0"

def test_s1_equals_s2():
    assert get_max_repetitions("ab", 3, "ab", 1) == 3, "s1 and s2 are identical"