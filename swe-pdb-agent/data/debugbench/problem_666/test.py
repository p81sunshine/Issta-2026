from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4

def test_no_forbidden():
    assert longestValidSubstring("abc", []) == 3

def test_all_chars_forbidden():
    assert longestValidSubstring("abc", ["a", "b", "c"]) == 0

def test_full_word_forbidden():
    assert longestValidSubstring("ab", ["ab"]) == 1