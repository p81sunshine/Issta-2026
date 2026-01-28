from solution import *

def test_example_1():
    assert smallestString("cbabc") == "baabc"

def test_example_2():
    assert smallestString("acbbc") == "abaab"

def test_example_3():
    assert smallestString("leetcode") == "kddsbncd"

def test_all_a():
    assert smallestString("a") == "z"
    assert smallestString("aa") == "az"
    assert smallestString("aaaa") == "aaaz"

def test_leading_a_non_a():
    assert smallestString("ab") == "aa"