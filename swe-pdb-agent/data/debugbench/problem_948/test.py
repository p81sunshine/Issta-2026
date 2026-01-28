from solution import *

def test_example_1():
    result = longestValidSubstring("cbaaaabc", ["aaa","cb"])
    assert result == 4, "Failed for example 1"

def test_example_2():
    result = longestValidSubstring("leetcode", ["de","le","e"])
    assert result == 4, "Failed for example 2"

def test_empty_forbidden():
    result = longestValidSubstring("abc", [])
    assert result == 3, "Failed for empty forbidden list"

def test_full_forbidden():
    result = longestValidSubstring("aaa", ["aaa"])
    assert result == 2, "Failed for fully forbidden word"

def test_multiple_forbidden_substrings():
    result = longestValidSubstring("abc", ["abc", "ab"])
    assert result == 2, "Failed for multiple forbidden substrings"