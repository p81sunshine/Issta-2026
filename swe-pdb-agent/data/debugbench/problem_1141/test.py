from solution import *

def test_example_1():
    assert getLengthOfOptimalCompression("aaabcccd", 2) == 4, "Example 1 failed"

def test_example_2():
    assert getLengthOfOptimalCompression("aabbaa", 2) == 2, "Example 2 failed"

def test_example_3():
    assert getLengthOfOptimalCompression("aaaaaaaaaaa", 0) == 3, "Example 3 failed"

def test_single_char():
    assert getLengthOfOptimalCompression("a", 0) == 1, "Single character test failed"

def test_delete_all():
    assert getLengthOfOptimalCompression("abc", 3) == 0, "Delete all characters test failed"