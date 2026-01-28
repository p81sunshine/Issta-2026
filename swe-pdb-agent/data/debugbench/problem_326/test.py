from solution import *

def test_example_1():
    assert smallestString("cbabc") == "baabc"

def test_example_2():
    assert smallestString("acbbc") == "abaab"

def test_example_3():
    assert smallestString("leetcode") == "kddsbncd"

def test_edge_case_single_a():
    assert smallestString("a") == "z"

def test_edge_case_leading_a():
    assert smallestString("ab") == "aa"