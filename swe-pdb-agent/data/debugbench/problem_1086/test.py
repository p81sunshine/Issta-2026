from solution import *

def test_example_1():
    assert makeSmallestPalindrome("egcfe") == "efcfe", "Failed for input 'egcfe'"

def test_example_2():
    assert makeSmallestPalindrome("abcd") == "abba", "Failed for input 'abcd'"

def test_example_3():
    assert makeSmallestPalindrome("seven") == "neven", "Failed for input 'seven'"

def test_single_char():
    assert makeSmallestPalindrome("a") == "a", "Failed for single character input"

def test_two_chars():
    assert makeSmallestPalindrome("ab") == "aa", "Failed for two-character input"