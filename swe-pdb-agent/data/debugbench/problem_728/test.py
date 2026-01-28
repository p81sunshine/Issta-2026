from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4, "Failed on first example"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4, "Failed on second example"

def test_no_forbidden():
    assert longestValidSubstring("abc", []) == 3, "Should return full length when forbidden is empty"

def test_full_forbidden():
    assert longestValidSubstring("aaa", ["aaa"]) == 2, "Should handle substring entirely in forbidden"

def test_forbidden_single_char():
    assert longestValidSubstring("ab", ["a"]) == 1, "Should handle forbidden single character"