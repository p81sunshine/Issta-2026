from solution import *

def test_example_1():
    assert isScramble("great", "rgeat") is True, "Example 1 should return True"

def test_example_2():
    assert isScramble("abcde", "caebd") is False, "Example 2 should return False"

def test_example_3():
    assert isScramble("a", "a") is True, "Example 3 should return True"

def test_edge_case_empty_strings():
    assert isScramble("", "") is True, "Empty strings should be scrambles"

def test_edge_case_single_mismatch():
    assert isScramble("a", "b") is False, "Single character mismatch should return False"