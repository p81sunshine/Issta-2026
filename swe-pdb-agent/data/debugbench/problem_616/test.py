from solution import *

def test_example_1():
    assert arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) is True, "Should return True for equal concatenated strings"

def test_example_2():
    assert arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) is False, "Should return False for different order"

def test_example_3():
    assert arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) is True, "Should return True for multi-segment match"

def test_edge_case_order_sensitivity():
    assert arrayStringsAreEqual(["x", "y"], ["xy"]) is True, "Should handle simple two-part concatenation"

def test_edge_case_empty_lists():
    assert arrayStringsAreEqual([], []) is True, "Empty lists should be equal"
    assert arrayStringsAreEqual([], ["a"]) is False, "Empty vs non-empty should not be equal"
    assert arrayStringsAreEqual(["a"], []) is False, "Non-empty vs empty should not be equal"