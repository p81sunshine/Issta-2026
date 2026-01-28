from solution import *

def test_example_1():
    assert get_max_repetions("acb", 4, "ab", 2) == 2

def test_example_2():
    assert get_max_repetions("acb", 1, "acb", 1) == 1

def test_no_characters():
    assert get_max_repetions("abc", 3, "abd", 1) == 0

def test_exact_match():
    assert get_max_repetions("ab", 3, "ab", 1) == 3

def test_cycle_case():
    assert get_max_repetions("ab", 5, "ab", 2) == 2

def test_edge_case_zero_n1():
    assert get_max_repetions("a", 0, "a", 1) == 0