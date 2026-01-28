from solution import *

def test_example_1():
    assert getLengthOfOptimalCompression("aaabcccd", 2) == 4, "Example 1 failed"

def test_example_2():
    assert getLengthOfOptimalCompression("aabbaa", 2) == 2, "Example 2 failed"

def test_example_3():
    assert getLengthOfOptimalCompression("aaaaaaaaaaa", 0) == 3, "Example 3 failed"

def test_delete_all():
    assert getLengthOfOptimalCompression("a", 1) == 0, "Delete all characters failed"
    assert getLengthOfOptimalCompression("abc", 3) == 0, "Delete all characters failed"

def test_unique_chars():
    assert getLengthOfOptimalCompression("abcd", 0) == 4, "Unique characters case failed"