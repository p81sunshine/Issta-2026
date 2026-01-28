from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4, "Example 1 failed"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4, "Example 2 failed"

def test_forbidden_empty():
    assert longestValidSubstring("abc", []) == 3, "Forbidden list empty test failed"

def test_entire_word_forbidden():
    assert longestValidSubstring("aaa", ["aaa"]) == 2, "Entire word forbidden test failed"

def test_forbidden_longer_than_substring():
    assert longestValidSubstring("ab", ["abcd"]) == 2, "Forbidden longer than substring test failed"