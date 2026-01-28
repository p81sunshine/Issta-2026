from solution import *

def test_case_1():
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    expected = sorted([0, 9])
    result = sorted(findSubstring(s, words))
    assert result == expected, f"Expected {expected} but got {result}"

def test_case_2():
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    expected = []
    assert findSubstring(s, words) == expected, "Expected empty list for invalid concatenation"

def test_case_3():
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    expected = sorted([6, 9, 12])
    result = sorted(findSubstring(s, words))
    assert result == expected, f"Expected {expected} but got {result}"

def test_insufficient_length():
    s = "a"
    words = ["a", "b"]
    expected = []
    assert findSubstring(s, words) == expected, "Should return empty list when input is too short"

def test_duplicate_words():
    s = "aaaaaa"
    words = ["aaa", "aaa"]
    expected = [0]
    result = sorted(findSubstring(s, words))
    assert result == expected, f"Expected {[0]} but got {result}"