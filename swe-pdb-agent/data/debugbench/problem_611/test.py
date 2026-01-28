from solution import *

def test_example_1():
    assert arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) is True

def test_example_2():
    assert arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) is False

def test_example_3():
    assert arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) is True

def test_order_sensitivity():
    assert arrayStringsAreEqual(["a", "b", "c"], ["abc"]) is True