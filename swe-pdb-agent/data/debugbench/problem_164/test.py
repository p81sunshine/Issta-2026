from solution import *

def test_example_1():
    assert isScramble("great", "rgeat") is True, "Should return True for valid scramble"

def test_example_2():
    assert isScramble("abcde", "caebd") is False, "Should return False for invalid scramble"

def test_example_3():
    assert isScramble("a", "a") is True, "Single character should be scramble of itself"

def test_substring_swap_case():
    assert isScramble("abc", "bca") is True, "Should handle cases requiring substring swap during recursion"