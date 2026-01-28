from solution import *

def test_example_1():
    assert arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) is True, "Example 1 failed"

def test_example_2():
    assert arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) is False, "Example 2 failed"

def test_example_3():
    assert arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) is True, "Example 3 failed"

def test_order_sensitivity():
    assert arrayStringsAreEqual(["a", "b"], ["ab"]) is True, "Order sensitivity test failed"

def test_empty_lists():
    assert arrayStringsAreEqual([], []) is True, "Empty lists comparison failed"