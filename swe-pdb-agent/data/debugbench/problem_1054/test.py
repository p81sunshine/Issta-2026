from solution import *

def test_example_1():
    assert sortString("aaaabbbbcccc") == "abccbaabccba", "Example 1 failed"

def test_example_2():
    assert sortString("rat") == "art", "Example 2 failed"

def test_edge_case_ab():
    assert sortString("ab") == "ab", "Edge case 'ab' failed"

def test_edge_case_aabb():
    assert sortString("aabb") == "abba", "Edge case 'aabb' failed"

def test_edge_empty():
    assert sortString("") == "", "Edge case empty string failed"