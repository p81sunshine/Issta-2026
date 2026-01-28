from solution import *

def test_example_1():
    assert longestWPI([9,9,6,0,6,6,9]) == 3, "Failed for example 1"

def test_example_2():
    assert longestWPI([6,6,6]) == 0, "Failed for example 2"

def test_empty_input():
    assert longestWPI([]) == 0, "Failed for empty input case"

def test_single_valid_input():
    assert longestWPI([9]) == 1, "Failed for single valid element"

def test_full_valid_array():
    assert longestWPI([9, 9, 9]) == 3, "Failed for fully valid array"