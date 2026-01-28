from solution import *

def test_example_1():
    assert getLengthOfOptimalCompression("aaabcccd", 2) == 4, "Example 1 failed"

def test_example_2():
    assert getLengthOfOptimalCompression("aabbaa", 2) == 2, "Example 2 failed"

def test_example_3():
    assert getLengthOfOptimalCompression("aaaaaaaaaaa", 0) == 3, "Example 3 failed"

def test_edge_case_1():
    assert getLengthOfOptimalCompression("a", 1) == 0, "Edge case 1 failed"

def test_edge_case_2():
    assert getLengthOfOptimalCompression("ab", 0) == 2, "Edge case 2 failed"