from solution import *

def test_example_1():
    assert smallestString("cbabc") == "baabc", "Failed for input 'cbabc'"

def test_example_2():
    assert smallestString("acbbc") == "abaab", "Failed for input 'acbbc'"

def test_example_3():
    assert smallestString("leetcode") == "kddsbncd", "Failed for input 'leetcode'"

def test_all_a():
    assert smallestString("aaaa") == "aaaz", "Failed for all 'a's input"

def test_single_a():
    assert smallestString("a") == "z", "Failed for single 'a' input"

def test_all_non_a():
    assert smallestString("zzzz") == "yyyy", "Failed for all non-a input"

def test_mixed_after_leading_a():
    assert smallestString("abba") == "aaaa", "Failed for mixed after leading a input"