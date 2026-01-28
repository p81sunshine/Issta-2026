from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4, "Example 1 failed"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4, "Example 2 failed"

def test_no_forbidden():
    assert longestValidSubstring("abc", []) == 3, "Empty forbidden list test failed"

def test_all_forbidden():
    assert longestValidSubstring("aaa", ["a"]) == 0, "All characters forbidden test failed"

def test_full_substring_forbidden():
    assert longestValidSubstring("abcd", ["abcd"]) == 3, "Full substring forbidden test failed"