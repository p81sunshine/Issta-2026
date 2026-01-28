from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed: should return 2 for 4*acb -> 2*ab*2"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed: should return 1 for 1*acb -> 1*acb*1"

def test_missing_characters():
    assert get_max_repetitions("abc", 5, "abd", 1) == 0, "Test missing characters: should return 0 when s2 contains characters not in s1"

def test_insufficient_repetitions():
    assert get_max_repetitions("ab", 1, "abab", 1) == 0, "Test insufficient repetitions: s1 can't form s2 even once"

def test_exact_match():
    assert get_max_repetitions("abc", 1, "abc", 1) == 1, "Test exact match: should return 1 for direct match"