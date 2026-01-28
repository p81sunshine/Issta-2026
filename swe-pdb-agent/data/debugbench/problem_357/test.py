from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4

def test_forbidden_exact_match():
    assert longestValidSubstring("ab", ["ab"]) == 1

def test_empty_forbidden():
    assert longestValidSubstring("test", []) == 4

def test_forbidden_longer_than_word():
    assert longestValidSubstring("abc", ["abcd"]) == 3