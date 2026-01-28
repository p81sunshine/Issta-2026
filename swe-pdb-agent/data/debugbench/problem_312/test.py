from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_no_common_characters():
    assert get_max_repetitions("abc", 5, "d", 1) == 0, "No common characters test failed"

def test_zero_n1():
    assert get_max_repetitions("abc", 0, "ab", 1) == 0, "Zero n1 test failed"

def test_direct_multiple():
    assert get_max_repetitions("ab", 3, "ab", 1) == 3, "Direct multiple test failed"