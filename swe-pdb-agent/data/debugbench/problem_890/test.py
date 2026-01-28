from solution import *

def test_example_1():
    assert isScramble("great", "rgeat") is True, "Failed for example 1"

def test_example_2():
    assert isScramble("abcde", "caebd") is False, "Failed for example 2"

def test_example_3():
    assert isScramble("a", "a") is True, "Failed for example 3"

def test_edge_case_1():
    assert isScramble("ab", "cd") is False, "Failed for edge case with length 2"