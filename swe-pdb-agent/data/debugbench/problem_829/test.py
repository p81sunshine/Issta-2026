from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4, "Example 1 failed"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4, "Example 2 failed"

def test_no_forbidden():
    assert longestValidSubstring("abc", []) == 3, "No forbidden words case failed"

def test_full_match():
    assert longestValidSubstring("abc", ["abc"]) == 2, "Full match forbidden case failed"

def test_all_forbidden():
    assert longestValidSubstring("ab", ["a", "b"]) == 0, "All forbidden case failed"