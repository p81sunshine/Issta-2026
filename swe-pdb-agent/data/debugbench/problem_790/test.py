from solution import *

def test_example_1():
    assert longestValidSubstring("cbaaaabc", ["aaa","cb"]) == 4, "Example 1 failed"

def test_example_2():
    assert longestValidSubstring("leetcode", ["de","le","e"]) == 4, "Example 2 failed"

def test_edge_empty_forbidden():
    assert longestValidSubstring("abc", []) == 3, "Empty forbidden list failed"

def test_edge_all_forbidden():
    assert longestValidSubstring("aaaaa", ["a"]) == 0, "All characters forbidden failed"

def test_edge_forbidden_at_end():
    assert longestValidSubstring("abc", ["bc"]) == 2, "Forbidden substring at end failed"

def test_edge_long_forbidden():
    assert longestValidSubstring("aaaaa", ["aaa"]) == 2, "Long forbidden substring failed"