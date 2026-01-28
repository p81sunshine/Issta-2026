from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4, "Example 1 failed"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4, "Example 2 failed"

def test_empty_forbidden():
    assert longestValidSubstring("abc", []) == 3, "Empty forbidden test failed"

def test_forbidden_single_char():
    assert longestValidSubstring("abc", ["b"]) == 1, "Forbidden single char test failed"

def test_no_valid_substrings():
    assert longestValidSubstring("aaa", ["a"]) == 0, "No valid substrings test failed"