from solution import *

def test_example_1():
    assert getLengthOfOptimalCompression("aaabcccd", 2) == 4

def test_example_2():
    assert getLengthOfOptimalCompression("aabbaa", 2) == 2

def test_example_3():
    assert getLengthOfOptimalCompression("aaaaaaaaaaa", 0) == 3

def test_delete_all():
    assert getLengthOfOptimalCompression("abc", 3) == 0

def test_single_char_no_deletion():
    assert getLengthOfOptimalCompression("a", 0) == 1