from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa", "cb"]) == 4, "First example should return 4"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de", "le", "e"]) == 4, "Second example should return 4"

def test_empty_forbidden():
    assert longestValidSubstring("abc", []) == 3, "Empty forbidden list should return the length of the word"

def test_single_char_forbidden():
    assert longestValidSubstring("abc", ["a"]) == 2, "Single character forbidden should return length of valid substring"