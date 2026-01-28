from solution import *

def test_example_1():
    assert minSteps("leetcode", "coats") == 7, "Example 1 failed"

def test_example_2():
    assert minSteps("night", "thing") == 0, "Example 2 failed"

def test_edge_case_empty():
    assert minSteps("", "") == 0, "Empty strings should require 0 steps"

def test_edge_case_single_char():
    assert minSteps("a", "") == 1, "Single char vs empty"
    assert minSteps("", "a") == 1, "Empty vs single char"

def test_case_unbalanced_counts():
    assert minSteps("ab", "abc") == 1, "Unbalanced counts case"