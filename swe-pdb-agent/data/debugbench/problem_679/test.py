from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4

def test_empty_forbidden():
    assert longestValidSubstring("abc", []) == 3

def test_full_forbidden():
    assert longestValidSubstring("aaa", ["aaa"]) == 2

def test_mixed_forbidden():
    assert longestValidSubstring("ababc", ["ab", "abc"]) == 2