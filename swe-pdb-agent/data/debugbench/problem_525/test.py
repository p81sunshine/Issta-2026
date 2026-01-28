from solution import *

def test_example_1():
    words = ["abc","car","ada","racecar","cool"]
    assert firstPalindrome(words) == "ada", "Failed for example 1"

def test_example_2():
    words = ["notapalindrome","racecar"]
    assert firstPalindrome(words) == "racecar", "Failed for example 2"

def test_example_3():
    words = ["def","ghi"]
    assert firstPalindrome(words) == "", "Failed for example 3"

def test_buggy_case_detection():
    words = ["aab", "ada"]
    assert firstPalindrome(words) == "ada", "Failed to detect buggy logic with sorted check"

def test_single_palindrome():
    words = ["aba"]
    assert firstPalindrome(words) == "aba", "Failed for single palindrome case"