from solution import *

def test_example_1():
    assert longestPrefix("level") == "l", "Example 1: 'level' should return 'l'"

def test_example_2():
    assert longestPrefix("ababab") == "abab", "Example 2: 'ababab' should return 'abab'"

def test_aabaab_case():
    assert longestPrefix("aabaab") == "aab", "Test case 'aabaab' should return 'aab'"

def test_all_same_characters():
    assert longestPrefix("aaaaa") == "aaaa", "Test case 'aaaaa' should return 'aaaa'"

def test_no_match_case():
    assert longestPrefix("abc") == "", "Test case 'abc' should return empty string"