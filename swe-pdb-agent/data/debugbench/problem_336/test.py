from solution import *

def test_example_1():
    assert countAnagrams("too hot") == 18, "Example 1 failed"

def test_example_2():
    assert countAnagrams("aa") == 1, "Example 2 failed"

def test_single_word_unique_letters():
    assert countAnagrams("abc") == 6, "Single word with unique letters failed"

def test_word_with_multiple_duplicates():
    assert countAnagrams("aabb") == 6, "Word 'aabb' should have 6 anagrams"

def test_edge_case_empty_string():
    assert countAnagrams("") == 1, "Empty string should return 1"