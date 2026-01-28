from solution import *

def test_example_1():
    assert countAnagrams("too hot") == 18, "Failed for input 'too hot'"

def test_example_2():
    assert countAnagrams("aa") == 1, "Failed for input 'aa'"

def test_aab():
    assert countAnagrams("aab") == 3, "Failed for input 'aab'"

def test_aaa():
    assert countAnagrams("aaa") == 1, "Failed for input 'aaa'"

def test_multiple_words():
    assert countAnagrams("aab aaa") == 3, "Failed for input 'aab aaa'"