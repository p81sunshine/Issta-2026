from solution import *

def test_example_1():
    assert get_max_repetions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_s2_has_extra_char():
    assert get_max_repetions("abc", 5, "abd", 1) == 0, "s2 has extra char failed"

def test_n1_zero():
    assert get_max_repetions("a", 0, "a", 1) == 0, "n1=0 edge case failed"

def test_cycle_handling():
    assert get_max_repetions("ab", 2, "ab", 1) == 2, "Cycle calculation failed"