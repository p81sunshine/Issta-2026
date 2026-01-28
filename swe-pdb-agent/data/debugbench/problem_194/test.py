from solution import *

def test_example_1():
    assert minDistance("horse", "ros") == 3, "Example 1 failed"

def test_example_2():
    assert minDistance("intention", "execution") == 5, "Example 2 failed"

def test_same_strings():
    assert minDistance("abc", "abc") == 0, "Same strings should have 0 distance"

def test_substring_deletion():
    assert minDistance("abc", "ab") == 1, "Deletion of single character failed"

def test_empty_to_nonempty():
    assert minDistance("", "a") == 1, "Empty to non-empty string failed"