from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_no_common_characters():
    assert get_max_repetitions("abc", 5, "abd", 1) == 0, "No common chars case failed"

def test_n1_zero():
    assert get_max_repetitions("abc", 0, "a", 1) == 0, "n1 zero case failed"

def test_direct_match():
    assert get_max_repetitions("ab", 3, "ab", 1) == 3, "Direct match case failed"