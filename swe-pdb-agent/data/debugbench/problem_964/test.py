from solution import *

def test_example_1():
    assert count_characters(["cat","bt","hat","tree"], "atach") == 6, "Example 1 failed"

def test_example_2():
    assert count_characters(["hello","world","leetcode"], "welldonehoneyr") == 10, "Example 2 failed"

def test_empty_words():
    assert count_characters([], "abc") == 0, "Empty words list should return 0"

def test_exact_match():
    assert count_characters(["aa"], "aa") == 2, "Exact character match failed"

def test_exceeding_characters():
    assert count_characters(["abb"], "ab") == 0, "Word with exceeding characters should be excluded"