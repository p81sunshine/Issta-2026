from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4, "Example 1 failed"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4, "Example 2 failed"

def test_empty_forbidden():
    assert longestValidSubstring("abc", []) == 3, "Empty forbidden list failed"

def test_forbidden_single_char():
    assert longestValidSubstring("aab", ["a"]) == 1, "Forbidden single character test failed"

def test_full_word_forbidden():
    assert longestValidSubstring("abc", ["abc"]) == 2, "Full word forbidden test failed"