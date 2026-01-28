from solution import *

def test_example_1():
    assert getLengthOfOptimalCompression("aaabcccd", 2) == 4, "Failed for case with optimal deletions of non-repeating chars"

def test_example_2():
    assert getLengthOfOptimalCompression("aabbaa", 2) == 2, "Failed for case with middle characters deletion"

def test_example_3():
    assert getLengthOfOptimalCompression("aaaaaaaaaaa", 0) == 3, "Failed for no deletions allowed with long repeated string"

def test_all_deletions():
    assert getLengthOfOptimalCompression("abc", 3) == 0, "Failed for full deletion scenario"