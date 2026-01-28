from solution import *

def test_example_1():
    assert makeSmallestPalindrome("egcfe") == "efcfe", "Example 1 failed"

def test_example_2():
    assert makeSmallestPalindrome("abcd") == "abba", "Example 2 failed"

def test_example_3():
    assert makeSmallestPalindrome("seven") == "neven", "Example 3 failed"

def test_single_char():
    assert makeSmallestPalindrome("a") == "a", "Single character test failed"

def test_two_chars():
    assert makeSmallestPalindrome("ab") == "aa", "Two characters test failed"

def test_odd_length():
    assert makeSmallestPalindrome("abc") == "aba", "Odd-length string test failed"