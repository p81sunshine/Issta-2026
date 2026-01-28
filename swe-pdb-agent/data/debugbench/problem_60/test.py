from solution import *

def test_example_1():
    assert arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) is True, "Example 1: ['ab','c'] vs ['a','bc'] should be equal"

def test_example_2():
    assert arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) is False, "Example 2: ['a','cb'] vs ['ab','c'] should not be equal"

def test_example_3():
    assert arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) is True, "Example 3: ['abc','d','defg'] vs ['abcddefg'] should be equal"

def test_single_element_vs_multiple():
    assert arrayStringsAreEqual(["a", "b"], ["ab"]) is True, "Single joined string vs split elements should be equal"

def test_empty_list_and_empty_string():
    assert arrayStringsAreEqual([], [""]) is True, "Empty list vs list with empty string should be equal"