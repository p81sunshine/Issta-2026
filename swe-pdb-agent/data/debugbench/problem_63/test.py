from solution import *

def test_example_1():
    assert longestPrefix("level") == "l", "Failed for input 'level'"

def test_example_2():
    assert longestPrefix("ababab") == "abab", "Failed for input 'ababab'"

def test_all_same_characters():
    assert longestPrefix("aaaaa") == "aaaa", "Failed for all identical characters"

def test_no_overlap_case():
    assert longestPrefix("abc") == "", "Failed for no common prefix/suffix"

def test_single_character():
    assert longestPrefix("a") == "", "Failed for single-character input"