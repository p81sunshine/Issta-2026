from solution import *

def test_example_1():
    assert longestPrefix("level") == "l", "Example 1: 'level' should return 'l'"

def test_example_2():
    assert longestPrefix("ababab") == "abab", "Example 2: 'ababab' should return 'abab'"

def test_edge_case_1():
    assert longestPrefix("aaabaaa") == "aaa", "Edge case: 'aaabaaa' should return 'aaa'"

def test_edge_case_2():
    assert longestPrefix("a") == "", "Edge case: 'a' should return empty string"

def test_edge_case_3():
    assert longestPrefix("abc") == "", "Edge case: 'abc' should return empty string"