from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa", "cb"]) == 4

def test_example_2():
    assert longestValidSubstring("leetcode", ["de", "le", "e"]) == 4

def test_forbidden_suffix():
    assert longestValidSubstring("aab", ["ab"]) == 2

def test_forbidden_in_middle():
    assert longestValidSubstring("aaab", ["aab"]) == 3

def test_empty_forbidden():
    assert longestValidSubstring("abc", []) == 3