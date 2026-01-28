from solution import *

def test_example_1():
    word = "cbaaaabc"
    forbidden = ["aaa", "cb"]
    assert longestValidSubstring(word, forbidden) == 4, "Failed for example 1"

def test_example_2():
    word = "leetcode"
    forbidden = ["de", "le", "e"]
    assert longestValidSubstring(word, forbidden) == 4, "Failed for example 2"

def test_forbidden_at_end():
    word = "abcd"
    forbidden = ["d"]
    assert longestValidSubstring(word, forbidden) == 3, "Failed when forbidden at end"

def test_forbidden_in_middle():
    word = "abc"
    forbidden = ["bc"]
    assert longestValidSubstring(word, forbidden) == 2, "Failed when forbidden in middle"