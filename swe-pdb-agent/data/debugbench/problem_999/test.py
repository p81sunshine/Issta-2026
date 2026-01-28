from solution import *

def test_example_1():
    assert minDistance("sea", "eat") == 2, "Failed for example case 1"

def test_example_2():
    assert minDistance("leetcode", "etco") == 4, "Failed for example case 2"

def test_equal_strings():
    assert minDistance("abc", "abc") == 0, "Failed for equal strings case"

def test_empty_to_non_empty():
    assert minDistance("", "abc") == 3, "Failed for empty to non-empty case"

def test_both_empty():
    assert minDistance("", "") == 0, "Failed for both empty case"