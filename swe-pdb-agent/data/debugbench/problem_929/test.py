from solution import *

def test_example_1():
    assert getLengthOfOptimalCompression("aaabcccd", 2) == 4, "Failed for example 1"

def test_example_2():
    assert getLengthOfOptimalCompression("aabbaa", 2) == 2, "Failed for example 2"

def test_example_3():
    assert getLengthOfOptimalCompression("aaaaaaaaaaa", 0) == 3, "Failed for example 3"

def test_all_deletions():
    assert getLengthOfOptimalCompression("abc", 3) == 0, "Failed for all deletions case"

def test_no_deletions_unique():
    assert getLengthOfOptimalCompression("abc", 0) == 3, "Failed for no deletions with unique characters"