from solution import *

def test_example_1():
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    assert isAlienSorted(words, order) is True, "Example 1 should return True"

def test_example_2():
    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    assert isAlienSorted(words, order) is False, "Example 2 should return False"

def test_example_3():
    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert isAlienSorted(words, order) is False, "Example 3 should return False"

def test_substring_shorter_first():
    words = ["aa", "a"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert isAlienSorted(words, order) is False, "Shorter substring case should return False"