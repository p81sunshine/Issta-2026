from solution import *

def test_example_1():
    assert arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) is True, "Example 1 should return True"

def test_example_2():
    assert arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) is False, "Example 2 should return False"

def test_example_3():
    assert arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) is True, "Example 3 should return True"

def test_edge_empty_lists():
    assert arrayStringsAreEqual([], []) is True, "Empty lists should be equal"

def test_edge_single_element():
    assert arrayStringsAreEqual(["xyz"], ["xyz"]) is True, "Single-element lists should match"

def test_edge_with_empty_string():
    assert arrayStringsAreEqual(["a", ""], ["a"]) is True, "Should handle empty string concatenation"