from solution import *

def test_example_1():
    words = ["abc","car","ada","racecar","cool"]
    assert firstPalindrome(words) == "ada", "First example failed"

def test_example_2():
    words = ["notapalindrome","racecar"]
    assert firstPalindrome(words) == "racecar", "Second example failed"

def test_example_3():
    words = ["def","ghi"]
    assert firstPalindrome(words) == "", "Third example failed"

def test_empty_input():
    assert firstPalindrome([]) == "", "Empty list should return empty string"

def test_immediate_palindrome():
    words = ["madam"]
    assert firstPalindrome(words) == "madam", "Single palindrome case failed"