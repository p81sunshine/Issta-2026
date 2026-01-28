from solution import *

def test_example_1():
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    expected = 6
    assert count_characters(words, chars) == expected, "Example 1 should return 6"

def test_example_2():
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    expected = 10
    assert count_characters(words, chars) == expected, "Example 2 should return 10"

def test_empty_words():
    words = []
    chars = "test"
    expected = 0
    assert count_characters(words, chars) == expected, "Empty words list should return 0"

def test_single_word():
    words = ["abc"]
    chars = "abc"
    expected = 3
    assert count_characters(words, chars) == expected, "Single word with matching chars should return length of word"

def test_insufficient_chars():
    words = ["aa"]
    chars = "a"
    expected = 0
    assert count_characters(words, chars) == expected, "Word with more chars than available should return 0"