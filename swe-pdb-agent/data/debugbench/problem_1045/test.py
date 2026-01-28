from solution import *

def test_example_1():
    assert countAnagrams("too hot") == 18, "Example 1: 'too hot' should return 18"

def test_example_2():
    assert countAnagrams("aa") == 1, "Example 2: 'aa' should return 1"

def test_all_unique_letters():
    assert countAnagrams("abc") == 6, "All unique letters in word should return factorial of length"

def test_multiple_duplicate_words():
    assert countAnagrams("aab baa") == 9, "Words with duplicates should multiply their respective permutations"

def test_all_same_characters():
    assert countAnagrams("aaa") == 1, "All same characters should return 1"