from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_no_common_characters():
    assert get_max_repetitions("abc", 5, "abd", 1) == 0, "No common characters case failed"

def test_n1_zero():
    assert get_max_repetitions("a", 0, "a", 1) == 0, "n1=0 case failed"

def test_exact_match():
    assert get_max_repetitions("ab", 2, "ab", 1) == 2, "Exact match case failed"