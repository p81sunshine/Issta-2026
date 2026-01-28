from solution import *

def test_example_1():
    assert smallestString("cbabc") == "baabc", "Example 1 failed"

def test_example_2():
    assert smallestString("acbbc") == "abaab", "Example 2 failed"

def test_example_3():
    assert smallestString("leetcode") == "kddsbncd", "Example 3 failed"

def test_edge_case_all_a():
    assert smallestString("aaaa") == "aaaz", "All 'a's case failed"

def test_edge_case_ba():
    assert smallestString("ba") == "aa", "Edge case 'ba' failed"

def test_edge_case_ab():
    assert smallestString("ab") == "aa", "Edge case 'ab' failed"