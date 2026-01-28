from solution import *

def test_example_1():
    words = ["abc","car","ada","racecar","cool"]
    assert firstPalindrome(words) == "ada", "Example 1 failed"

def test_example_2():
    words = ["notapalindrome","racecar"]
    assert firstPalindrome(words) == "racecar", "Example 2 failed"

def test_example_3():
    words = ["def","ghi"]
    assert firstPalindrome(words) == "", "Example 3 failed"

def test_empty_list():
    assert firstPalindrome([]) == "", "Empty list should return empty string"

def test_first_word_palindrome():
    assert firstPalindrome(["madam", "abc"]) == "madam", "First word is palindrome test failed"