from solution import *

def test_example_1():
    assert countAnagrams("too hot") == 18, "Failed for example input 'too hot'"

def test_example_2():
    assert countAnagrams("aa") == 1, "Failed for example input 'aa'"

def test_case_aab():
    assert countAnagrams("aab") == 3, "Failed for input 'aab' (duplicate characters)"

def test_case_abc():
    assert countAnagrams("abc") == 6, "Failed for input 'abc' (unique characters)"

def test_case_aabb():
    assert countAnagrams("aabb") == 6, "Failed for input 'aabb' (multiple duplicates)"