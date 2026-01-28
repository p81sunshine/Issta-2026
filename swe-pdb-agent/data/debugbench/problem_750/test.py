from solution import *

def test_example_1():
    assert getLengthOfOptimalCompression("aaabcccd", 2) == 4, "Example 1 failed"

def test_example_2():
    assert getLengthOfOptimalCompression("aabbaa", 2) == 2, "Example 2 failed"

def test_example_3():
    assert getLengthOfOptimalCompression("aaaaaaaaaaa", 0) == 3, "Example 3 failed"

def test_edge_case_delete_all():
    assert getLengthOfOptimalCompression("abc", 3) == 0, "Edge case: delete all characters failed"

def test_edge_case_k_zero_unique():
    assert getLengthOfOptimalCompression("abcd", 0) == 4, "Edge case: k=0 with all unique characters failed"