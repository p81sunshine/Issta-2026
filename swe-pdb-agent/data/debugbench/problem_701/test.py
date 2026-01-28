from solution import *

def test_example_1():
    assert getLengthOfOptimalCompression("aaabcccd", 2) == 4, "Example 1: Deleting 'b' and 'd' should yield length 4"

def test_example_2():
    assert getLengthOfOptimalCompression("aabbaa", 2) == 2, "Example 2: Deleting 'b's should yield 'a4' with length 2"

def test_example_3():
    assert getLengthOfOptimalCompression("aaaaaaaaaaa", 0) == 3, "Example 3: 'a11' has length 3"

def test_delete_all_chars():
    assert getLengthOfOptimalCompression("abcde", 5) == 0, "Deleting all characters should result in 0 length"

def test_single_char_edge_case():
    assert getLengthOfOptimalCompression("a", 0) == 1, "Single character with no deletions should return 1"