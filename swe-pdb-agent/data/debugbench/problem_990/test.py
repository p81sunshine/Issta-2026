from solution import *

def test_example_1():
    assert getLengthOfOptimalCompression("aaabcccd", 2) == 4, "Example 1 failed"

def test_example_2():
    assert getLengthOfOptimalCompression("aabbaa", 2) == 2, "Example 2 failed"

def test_example_3():
    assert getLengthOfOptimalCompression("aaaaaaaaaaa", 0) == 3, "Example 3 failed"

def test_edge_case_deletion_all():
    assert getLengthOfOptimalCompression("abc", 3) == 0, "Edge case: full deletion failed"

def test_edge_case_single_char():
    assert getLengthOfOptimalCompression("a", 0) == 1, "Edge case: single character failed"