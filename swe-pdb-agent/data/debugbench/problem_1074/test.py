from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa", "cb"]) == 4

def test_example_2():
    assert longestValidSubstring("leetcode", ["de", "le", "e"]) == 4

def test_simple_forbidden_match():
    assert longestValidSubstring("ab", ["ab"]) == 1

def test_multiple_forbidden_matches():
    assert longestValidSubstring("aaaa", ["aaa"]) == 2