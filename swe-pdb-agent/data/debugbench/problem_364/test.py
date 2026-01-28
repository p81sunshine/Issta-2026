from solution import *

def test_example_1():
    assert arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) is True, "Example 1: word1 and word2 should be equal"

def test_example_2():
    assert arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) is False, "Example 2: word1 and word2 should not be equal"

def test_example_3():
    assert arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) is True, "Example 3: word1 and word2 should be equal"

def test_empty_lists():
    assert arrayStringsAreEqual([], []), "Empty lists should be considered equal"

def test_empty_vs_non_empty():
    assert arrayStringsAreEqual([], ["a"]) is False, "Empty list vs non-empty list should not be equal"

def test_multiple_parts():
    assert arrayStringsAreEqual(["h", "e", "l", "l", "o"], ["hello"]) is True, "Concatenated parts should match single string"