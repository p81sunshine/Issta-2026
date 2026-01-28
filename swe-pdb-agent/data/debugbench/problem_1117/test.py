from solution import *

def test_example_1():
    assert count_characters(["cat","bt","hat","tree"], "atach") == 6

def test_example_2():
    assert count_characters(["hello","world","leetcode"], "welldonehoneyr") == 10

def test_empty_words():
    assert count_characters([], "any") == 0

def test_single_word():
    assert count_characters(["test"], "test") == 4

def test_no_match():
    assert count_characters(["abc"], "def") == 0