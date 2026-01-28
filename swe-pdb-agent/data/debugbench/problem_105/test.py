from solution import *

def test_example_1():
    assert sortString("aaaabbbbcccc") == "abccbaabccba", "Failed for multiple repeated characters"

def test_example_2():
    assert sortString("rat") == "art", "Failed for unique character set"

def test_edge_empty():
    assert sortString("") == "", "Failed for empty string input"

def test_edge_single():
    assert sortString("a") == "a", "Failed for single character input"

def test_two_chars_alternating():
    assert sortString("aabb") == "abba", "Failed for alternating two-character case"