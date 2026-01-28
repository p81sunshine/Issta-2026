from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 should return 2"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 should return 1"

def test_edge_case_1():
    assert get_max_repetitions("abc", 3, "abd", 1) == 0, "s2 contains 'd' not in s1 should return 0"

def test_edge_case_2():
    assert get_max_repetitions("abc", 0, "ab", 1) == 0, "n1=0 should return 0"

def test_edge_case_3():
    assert get_max_repetitions("a", 3, "aa", 1) == 1, "s1='a' n1=3 s2='aa' should return 1"