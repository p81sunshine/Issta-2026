from solution import *

def test_example_1():
    assert longest_valid_substring("cbaaaabc", ["aaa", "cb"]) == 4, "Example 1 failed"

def test_example_2():
    assert longest_valid_substring("leetcode", ["de","le","e"]) == 4, "Example 2 failed"

def test_empty_forbidden():
    assert longest_valid_substring("abc", []) == 3, "Empty forbidden list failed"

def test_all_chars_forbidden():
    assert longest_valid_substring("abc", ["a","b","c"]) == 0, "All characters forbidden failed"

def test_forbidden_longer_than_word():
    assert longest_valid_substring("ab", ["abc"]) == 2, "Forbidden substring longer than word failed"