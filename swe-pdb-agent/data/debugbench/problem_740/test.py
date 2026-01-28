from solution import *

def test_example_1():
    assert longest_valid_substring("cbaaaabc", ["aaa","cb"]) == 4, "Failed on example 1"

def test_example_2():
    assert longest_valid_substring("leetcode", ["de","le","e"]) == 4, "Failed on example 2"

def test_empty_forbidden():
    assert longest_valid_substring("abc", []) == 3, "Should return full length when forbidden is empty"

def test_full_forbidden():
    assert longest_valid_substring("aaa", ["aaa"]) == 2, "Longest valid substring when full match"

def test_single_forbidden():
    assert longest_valid_substring("a", ["a"]) == 0, "Single character forbidden case"