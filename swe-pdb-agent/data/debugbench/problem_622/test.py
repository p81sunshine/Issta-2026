from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4

def test_edge_empty_forbidden():
    assert longestValidSubstring("a", []) == 1

def test_entire_word_forbidden():
    assert longestValidSubstring("aaa", ["aaa"]) == 2

def test_forbidden_longer_than_word():
    assert longestValidSubstring("a", ["aa"]) == 1