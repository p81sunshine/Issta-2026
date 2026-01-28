from solution import *

def test_example_1():
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    expected = 6
    assert count_characters(words, chars) == expected, "Example 1 failed"

def test_example_2():
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    expected = 10
    assert count_characters(words, chars) == expected, "Example 2 failed"

def test_single_word():
    words = ["a"]
    chars = "a"
    expected = 1
    assert count_characters(words, chars) == expected, "Single word test failed"

def test_no_valid_words():
    words = ["abc", "defg"]
    chars = "xyz"
    expected = 0
    assert count_characters(words, chars) == expected, "No valid words test failed"

def test_all_valid_words():
    words = ["aa", "bb"]
    chars = "aabb"
    expected = 4
    assert count_characters(words, chars) == expected, "All valid words test failed"