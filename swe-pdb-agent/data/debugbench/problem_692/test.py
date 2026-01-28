from solution import *

def test_example_1():
    assert arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) is True, "Example 1 should return True"

def test_example_2():
    assert arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) is False, "Example 2 should return False"

def test_example_3():
    assert arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) is True, "Example 3 should return True"

def test_empty_lists():
    assert arrayStringsAreEqual([], []) is True, "Two empty lists should be equal"

def test_reversal_case():
    assert arrayStringsAreEqual(["x", "y"], ["xy"]) is True, "Reversed lists should not affect concatenation"