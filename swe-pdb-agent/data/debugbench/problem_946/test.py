from solution import *

def test_example_1():
    assert arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) is True

def test_example_2():
    assert arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) is False

def test_example_3():
    assert arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) is True

def test_reversed_order_case():
    assert arrayStringsAreEqual(["a", "b"], ["ab"]) is True

def test_reverse_mismatch_case():
    assert arrayStringsAreEqual(["b", "a"], ["a", "b"]) is False