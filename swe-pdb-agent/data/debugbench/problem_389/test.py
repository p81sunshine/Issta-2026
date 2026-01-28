from solution import *

def test_example_1():
    assert makeSmallestPalindrome("egcfe") == "efcfe", "Failed for example 1"

def test_example_2():
    assert makeSmallestPalindrome("abcd") == "abba", "Failed for example 2"

def test_example_3():
    assert makeSmallestPalindrome("seven") == "neven", "Failed for example 3"

def test_two_character_string():
    assert makeSmallestPalindrome("ba") == "aa", "Failed for two-character string"