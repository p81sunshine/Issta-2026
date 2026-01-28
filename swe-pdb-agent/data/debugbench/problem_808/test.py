from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4

def test_empty_forbidden():
    assert longestValidSubstring("abc", []) == 3

def test_forbidden_entire_word():
    assert longestValidSubstring("abc", ["abc"]) == 2

def test_forbidden_single_char():
    assert longestValidSubstring("a", ["a"]) == 0