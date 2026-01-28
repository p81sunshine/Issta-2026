from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4

def test_edge_case_single_forbidden():
    assert longestValidSubstring("ab", ["a"]) == 1

def test_edge_case_full_match():
    assert longestValidSubstring("a", ["a"]) == 0

def test_empty_forbidden():
    assert longestValidSubstring("anything", []) == 8

def test_forbidden_longer_than_word():
    assert longestValidSubstring("abc", ["abcd"]) == 3