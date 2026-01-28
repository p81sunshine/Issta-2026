from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa", "cb"]) == 4, "Example 1 should return 4"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de", "le", "e"]) == 4, "Example 2 should return 4"

def test_empty_forbidden():
    assert longestValidSubstring("abc", []) == 3, "When forbidden is empty, entire word is valid"

def test_word_is_forbidden():
    assert longestValidSubstring("a", ["a"]) == 0, "Word is forbidden, output should be 0"

def test_forbidden_not_in_word():
    assert longestValidSubstring("abc", ["abcd"]) == 3, "Forbidden substring not present, entire word is valid"