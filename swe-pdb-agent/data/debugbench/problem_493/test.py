from solution import *

def test_example_1():
    assert characterReplacement("ABAB", 2) == 4, "Example 1 failed"

def test_example_2():
    assert characterReplacement("AABABBA", 1) == 4, "Example 2 failed"

def test_all_same_characters():
    assert characterReplacement("ZZZZZ", 2) == 5, "All same characters test failed"

def test_zero_replacements():
    assert characterReplacement("AABBA", 0) == 2, "Zero replacements edge case failed"

def test_large_k():
    assert characterReplacement("ABCD", 10) == 4, "Large k test failed"

def test_single_character():
    assert characterReplacement("A", 100) == 1, "Single character test failed"