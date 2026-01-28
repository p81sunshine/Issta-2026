from solution import *

def test_example_1():
    assert min_distance("sea", "eat") == 2, "Example 1 failed: sea to eat should require 2 operations"

def test_example_2():
    assert min_distance("leetcode", "etco") == 4, "Example 2 failed: leetcode to etco should require 4 operations"

def test_identical_strings():
    assert min_distance("abc", "abc") == 0, "Identical strings should require 0 operations"

def test_empty_to_non_empty():
    assert min_distance("", "abc") == 3, "Empty to non-empty string should require length of target insertions"

def test_no_common_characters():
    assert min_distance("abc", "def") == 6, "Strings with no common characters should require sum of lengths operations"