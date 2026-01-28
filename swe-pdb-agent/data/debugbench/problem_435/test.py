from solution import *

def test_example_1():
    word = "cbaaaabc"
    forbidden = ["aaa","cb"]
    expected = 4
    assert longestValidSubstring(word, forbidden) == expected

def test_example_2():
    word = "leetcode"
    forbidden = ["de","le","e"]
    expected = 4
    assert longestValidSubstring(word, forbidden) == expected

def test_empty_forbidden():
    word = "abc"
    forbidden = []
    expected = 3
    assert longestValidSubstring(word, forbidden) == expected

def test_all_substrings_forbidden():
    word = "a"
    forbidden = ["a"]
    expected = 0
    assert longestValidSubstring(word, forbidden) == expected

def test_single_forbidden_char():
    word = "ab"
    forbidden = ["a"]
    expected = 1
    assert longestValidSubstring(word, forbidden) == expected