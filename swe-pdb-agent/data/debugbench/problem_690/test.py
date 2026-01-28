from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_no_common_characters():
    assert get_max_repetitions("abc", 3, "abd", 1) == 0, "No common characters test failed"

def test_exact_match():
    assert get_max_repetitions("ab", 3, "ab", 1) == 3, "Exact match test failed"

def test_division_case():
    assert get_max_repetitions("a", 5, "aa", 1) == 2, "Division case test failed"