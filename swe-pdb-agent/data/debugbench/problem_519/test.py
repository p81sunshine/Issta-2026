from solution import *

def test_example_1():
    assert longestPrefix("level") == "l", "Example 1 failed"

def test_example_2():
    assert longestPrefix("ababab") == "abab", "Example 2 failed"

def test_edge_case_empty():
    assert longestPrefix("a") == "", "Edge case with single character failed"

def test_case_multiple_overlaps():
    assert longestPrefix("aabaaab") == "aab", "Test case for overlapping prefixes/suffixes failed"