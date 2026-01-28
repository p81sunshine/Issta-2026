from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4

def test_empty_forbidden():
    assert longestValidSubstring("abc", []) == 3, "Empty forbidden list should return full length"

def test_forbidden_single_char_entire_word():
    assert longestValidSubstring("c", ["c"]) == 0, "Entire word is forbidden"

def test_forbidden_in_middle():
    assert longestValidSubstring("cb", ["cb"]) == 1, "Only substrings of length 1 are valid"