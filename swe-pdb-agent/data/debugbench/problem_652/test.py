from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4, "Example 1 failed"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4, "Example 2 failed"

def test_empty_forbidden():
    assert longestValidSubstring("abc", []) == 3, "Empty forbidden list test failed"

def test_forbidden_longer_than_word():
    assert longestValidSubstring("abc", ["abcdef"]) == 3, "Forbidden longer than word test failed"

def test_entire_word_forbidden():
    assert longestValidSubstring("aaa", ["aaa"]) == 2, "Entire word forbidden test failed"