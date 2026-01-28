from solution import *

def test_example_1():
    assert get_max_repetions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_cycle_condition_bug():
    # This case triggers the buggy condition (rec[-1] >= n1)
    assert get_max_repetions("ab", 2, "a", 2) == 1, "Cycle condition bug not caught"

def test_no_common_characters():
    assert get_max_repetions("abc", 5, "def", 1) == 0, "No common characters case failed"

def test_zero_n1():
    assert get_max_repetions("abc", 0, "a", 1) == 0, "Zero n1 case failed"