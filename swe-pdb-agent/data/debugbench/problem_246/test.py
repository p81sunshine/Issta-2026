from solution import *

def test_example_1():
    assert countAnagrams("too hot") == 18, "Example 1: 'too hot' should return 18"

def test_example_2():
    assert countAnagrams("aa") == 1, "Example 2: 'aa' should return 1"

def test_single_word_unique_letters():
    assert countAnagrams("abc") == 6, "Single word with unique letters (abc) should return 3! = 6"

def test_word_with_multiple_duplicates():
    assert countAnagrams("aab") == 3, "Word 'aab' should have 3!/(2!1!) = 3 anagrams"

def test_single_character():
    assert countAnagrams("a") == 1, "Single character 'a' should return 1"