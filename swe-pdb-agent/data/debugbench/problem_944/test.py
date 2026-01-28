from solution import *

def test_example_1():
    assert minDistance("horse", "ros") == 3, "Should return 3 operations for 'horse' to 'ros'"

def test_example_2():
    assert minDistance("intention", "execution") == 5, "Should return 5 operations for 'intention' to 'execution'"

def test_empty_strings():
    assert minDistance("", "") == 0, "Empty strings should have 0 distance"

def test_identical_strings():
    assert minDistance("abc", "abc") == 0, "Identical strings should have 0 distance"

def test_single_operation_replace():
    assert minDistance("a", "b") == 1, "Single character replacement should cost 1"