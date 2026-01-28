from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa", "cb"]) == 4, "Example 1 should return 4"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de", "le", "e"]) == 4, "Example 2 should return 4"

def test_empty_forbidden():
    assert longestValidSubstring("abc", []) == 3, "Empty forbidden list should return full length"

def test_forbidden_in_middle():
    assert longestValidSubstring("abcb", ["cb"]) == 3, "Forbidden substring in middle should return 3"

def test_forbidden_longer_substring():
    assert longestValidSubstring("aaaa", ["aaa"]) == 2, "Forbidden 'aaa' should return maximum valid length 2"