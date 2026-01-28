from solution import *

def test_example_1():
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    expected = [0, 9]
    assert findSubstring(s, words) == expected, "Test case 1 failed"

def test_example_2():
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    expected = []
    assert findSubstring(s, words) == expected, "Test case 2 failed"

def test_example_3():
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    expected = [6, 9, 12]
    assert findSubstring(s, words) == expected, "Test case 3 failed"

def test_edge_case_empty():
    s = "a"
    words = ["b"]
    expected = []
    assert findSubstring(s, words) == expected, "Edge case with no match failed"

def test_edge_case_single_word():
    s = "aaa"
    words = ["a"]
    expected = [0, 1, 2]
    assert findSubstring(s, words) == expected, "Edge case with single word failed"