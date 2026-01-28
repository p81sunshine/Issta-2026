from solution import *

def test_example_1():
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    expected = [0, 9]
    result = findSubstring(s, words)
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"

def test_example_2():
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    expected = []
    result = findSubstring(s, words)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_example_3():
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    expected = [6, 9, 12]
    result = findSubstring(s, words)
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"

def test_short_string():
    s = "ab"
    words = ["a", "b"]
    expected = [0]
    result = findSubstring(s, words)
    assert result == expected, f"Expected {expected}, but got {result}"