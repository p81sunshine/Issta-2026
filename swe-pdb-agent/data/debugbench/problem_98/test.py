from solution import *

def test_example_1():
    assert longestWPI([9,9,6,0,6,6,9]) == 3, "Example 1 failed"

def test_example_2():
    assert longestWPI([6,6,6]) == 0, "Example 2 failed"

def test_all_over_8():
    assert longestWPI([9,9,9]) == 3, "All elements over 8 failed"

def test_single_valid():
    assert longestWPI([9]) == 1, "Single valid element failed"

def test_empty_input():
    assert longestWPI([]) == 0, "Empty input edge case failed"