from solution import *

def test_example_1():
    assert longestPrefix("level") == "l", "Test case 1 failed: 'level' should return 'l'"

def test_example_2():
    assert longestPrefix("ababab") == "abab", "Test case 2 failed: 'ababab' should return 'abab'"

def test_all_same_characters():
    assert longestPrefix("aaaaa") == "aaaa", "Test case 3 failed: 'aaaaa' should return 'aaaa'"

def test_no_common_prefix_suffix():
    assert longestPrefix("abc") == "", "Test case 4 failed: 'abc' should return empty string"

def test_longer_abababab():
    assert longestPrefix("abababab") == "ababab", "Test case 5 failed: 'abababab' should return 'ababab'"