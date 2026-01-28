from solution import *

def test_example_1():
    assert array_strings_are_equal(["ab", "c"], ["a", "bc"]) is True, "Example 1 should return True"

def test_example_2():
    assert array_strings_are_equal(["a", "cb"], ["ab", "c"]) is False, "Example 2 should return False"

def test_example_3():
    assert array_strings_are_equal(["abc", "d", "defg"], ["abcddefg"]) is True, "Example 3 should return True"

def test_empty_lists():
    assert array_strings_are_equal([], []) is True, "Empty lists should return True"