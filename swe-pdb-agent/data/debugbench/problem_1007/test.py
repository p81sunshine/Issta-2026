from solution import *

def test_example_1():
    word = "cbaaaabc"
    forbidden = ["aaa","cb"]
    assert longestValidSubstring(word, forbidden) == 4, "Example 1 should return 4"

def test_example_2():
    word = "leetcode"
    forbidden = ["de","le","e"]
    assert longestValidSubstring(word, forbidden) == 4, "Example 2 should return 4"

def test_forbidden_single_char():
    word = "ab"
    forbidden = ["a"]
    assert longestValidSubstring(word, forbidden) == 1, "Should return 1 as 'b' is valid"

def test_all_forbidden():
    word = "aa"
    forbidden = ["a"]
    assert longestValidSubstring(word, forbidden) == 0, "All characters forbidden, max is 0"

def test_empty_forbidden():
    word = "abc"
    forbidden = []
    assert longestValidSubstring(word, forbidden) == 3, "No forbidden substrings, entire word is valid"