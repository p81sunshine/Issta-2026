from solution import *

def test_example_1():
    assert count_good_substrings("xyzzaz") == 1, "Failed on example 1"

def test_example_2():
    assert count_good_substrings("aababcabc") == 4, "Failed on example 2"

def test_short_string():
    assert count_good_substrings("abc") == 1, "Failed on 3-character string"

def test_all_duplicates():
    assert count_good_substrings("aaaaa") == 0, "Failed on all duplicates"

def test_mixed_cases():
    assert count_good_substrings("abcabc") == 4, "Failed on multiple valid substrings"