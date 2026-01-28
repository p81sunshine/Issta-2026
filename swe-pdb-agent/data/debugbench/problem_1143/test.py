from solution import *

def test_example_1():
    assert findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0,9], "Example 1 failed"

def test_example_2():
    assert findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) == [], "Example 2 failed"

def test_example_3():
    assert findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]) == [6,9,12], "Example 3 failed"

def test_edge_case_overlapping():
    assert findSubstring("aaaaa", ["aa","aa"]) == [0,1], "Edge case with overlapping substrings failed"