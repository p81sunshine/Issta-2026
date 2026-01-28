from solution import *

def test_example_1():
    assert count_characters(["cat","bt","hat","tree"], "atach") == 6, "Example 1 failed"

def test_example_2():
    assert count_characters(["hello","world","leetcode"], "welldonehoneyr") == 10, "Example 2 failed"

def test_empty_words():
    assert count_characters([], "abc") == 0, "Empty words test failed"

def test_single_word():
    assert count_characters(["a"], "a") == 1, "Single word test failed"