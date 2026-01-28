from solution import *

def test_example_1():
    word = "cbaaaabc"
    forbidden = ["aaa", "cb"]
    assert longestValidSubstring(word, forbidden) == 4, "Example 1 should return 4"

def test_example_2():
    word = "leetcode"
    forbidden = ["de", "le", "e"]
    assert longestValidSubstring(word, forbidden) == 4, "Example 2 should return 4"

def test_forbidden_single_char():
    word = "abcd"
    forbidden = ["d"]
    assert longestValidSubstring(word, forbidden) == 3, "Single forbidden character test should return 3"

def test_empty_forbidden():
    word = "abc"
    forbidden = []
    assert longestValidSubstring(word, forbidden) == 3, "Empty forbidden list should return full length"

def test_no_valid_substring():
    word = "aaa"
    forbidden = ["a", "aa", "aaa"]
    assert longestValidSubstring(word, forbidden) == 0, "All substrings forbidden should return 0"