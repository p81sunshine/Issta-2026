from solution import *

def test_example_1():
    assert minDistance("sea", "eat") == 2, "Example 1 failed"

def test_example_2():
    assert minDistance("leetcode", "etco") == 4, "Example 2 failed"

def test_edge_case_empty_strings():
    assert minDistance("abc", "") == 3, "Edge case: word2 empty failed"
    assert minDistance("", "def") == 3, "Edge case: word1 empty failed"