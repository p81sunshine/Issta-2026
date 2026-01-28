from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4, "Example 1 failed"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4, "Example 2 failed"

def test_edge_case_forbidden_empty():
    assert longestValidSubstring("abc", []) == 3, "Empty forbidden list test failed"

def test_edge_case_full_forbidden():
    assert longestValidSubstring("cb", ["cb"]) == 1, "Full forbidden substring test failed"

def test_edge_case_no_valid():
    assert longestValidSubstring("abc", ["a", "b", "c"]) == 0, "No valid substring test failed"