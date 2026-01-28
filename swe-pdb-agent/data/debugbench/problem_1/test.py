from solution import *

def test_example_1():
    assert sortString("aaaabbbbcccc") == "abccbaabccba", "Example 1 failed"

def test_example_2():
    assert sortString("rat") == "art", "Example 2 failed"

def test_even_counts():
    assert sortString("aabb") == "abba", "Even counts test case failed"

def test_single_char():
    assert sortString("a") == "a", "Single character test case failed"

def test_all_same_chars():
    assert sortString("aaaaa") == "aaaaa", "All same characters test case failed"