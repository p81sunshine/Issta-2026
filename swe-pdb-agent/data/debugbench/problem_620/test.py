from solution import *

def test_example_1():
    assert countAnagrams("too hot") == 18, "Example 1 failed"

def test_example_2():
    assert countAnagrams("aa") == 1, "Example 2 failed"

def test_single_word_unique_chars():
    assert countAnagrams("hot") == 6, "Test single word with unique chars failed"

def test_two_letter_word():
    assert countAnagrams("ab") == 2, "Test two-letter word failed"

def test_multiple_words_with_unique():
    assert countAnagrams("i am") == 2, "Test multiple words with unique chars failed"