from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4, "Example 1 failed"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4, "Example 2 failed"

def test_empty_forbidden():
    assert longestValidSubstring("abc", []) == 3, "Empty forbidden list test failed"

def test_full_forbidden():
    assert longestValidSubstring("aaa", ["a"]) == 0, "Full forbidden test failed"

def test_single_char_forbidden():
    assert longestValidSubstring("a", ["a"]) == 0, "Single character forbidden test failed"