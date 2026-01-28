from solution import *

def test_example_1():
    assert getLengthOfOptimalCompression("aaabcccd", 2) == 4, "Failed for case 1: optimal deletion of b and d"

def test_example_2():
    assert getLengthOfOptimalCompression("aabbaa", 2) == 2, "Failed for case 2: optimal deletion of both b's"

def test_example_3():
    assert getLengthOfOptimalCompression("aaaaaaaaaaa", 0) == 3, "Failed for case 3: cannot delete anything"

def test_all_deleted():
    assert getLengthOfOptimalCompression("abc", 3) == 0, "Failed for complete deletion scenario"

def test_single_char_no_delete():
    assert getLengthOfOptimalCompression("a", 0) == 1, "Failed for single character with no deletions"