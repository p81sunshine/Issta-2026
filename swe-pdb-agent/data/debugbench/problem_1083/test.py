from solution import *

def test_example_1():
    assert countAnagrams("too hot") == 18, "Example 1 failed"

def test_example_2():
    assert countAnagrams("aa") == 1, "Example 2 failed"

def test_single_letter():
    assert countAnagrams("a") == 1, "Single letter word failed"

def test_two_unique_letters():
    assert countAnagrams("ab") == 2, "Two unique letters calculation failed"

def test_empty_string():
    assert countAnagrams("") == 1, "Empty string edge case failed"