from solution import *

def test_example_1():
    assert make_smallest_palindrome("egcfe") == "efcfe", "Example 1 failed"

def test_example_2():
    assert make_smallest_palindrome("abcd") == "abba", "Example 2 failed"

def test_example_3():
    assert make_smallest_palindrome("seven") == "neven", "Example 3 failed"

def test_single_character():
    assert make_smallest_palindrome("a") == "a", "Single character test failed"

def test_two_characters():
    assert make_smallest_palindrome("ab") == "aa", "Two characters test failed"