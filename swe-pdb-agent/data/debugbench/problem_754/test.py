from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4, "Example 1 failed"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4, "Example 2 failed"

def test_no_forbidden():
    assert longestValidSubstring("hello", []) == 5, "No forbidden case failed"

def test_full_forbidden():
    assert longestValidSubstring("abc", ["abc"]) == 2, "Full forbidden case failed"

def test_overlapping_forbidden():
    assert longestValidSubstring("abac", ["ab", "ba"]) == 2, "Overlapping forbidden case failed"