from solution import *

def test_example_1():
    assert smallestString("cbabc") == "baabc", "Example 1 failed"

def test_example_2():
    assert smallestString("acbbc") == "abaab", "Example 2 failed"

def test_example_3():
    assert smallestString("leetcode") == "kddsbncd", "Example 3 failed"

def test_all_a():
    assert smallestString("aaaaa") == "aaaaz", "All 'a's case failed"

def test_single_a():
    assert smallestString("a") == "z", "Single 'a' case failed"

def test_mixed_leading_a():
    assert smallestString("aaz") == "aay", "Mixed leading 'a's case failed"