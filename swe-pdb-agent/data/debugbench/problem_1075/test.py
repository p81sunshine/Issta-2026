from solution import *

def test_example_1():
    assert arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) == True

def test_example_2():
    assert arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) == False

def test_example_3():
    assert arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) == True

def test_empty_lists():
    assert arrayStringsAreEqual([], []) == True

def test_empty_vs_non_empty():
    assert arrayStringsAreEqual([], ["a"]) == False

def test_empty_string_in_list():
    assert arrayStringsAreEqual(["a", ""], ["a"]) == True