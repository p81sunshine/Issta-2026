from solution import *

def test_example_1():
    assert countAnagrams("too hot") == 18, "Example 1 failed"

def test_example_2():
    assert countAnagrams("aa") == 1, "Example 2 failed"

def test_case_aab():
    assert countAnagrams("aab") == 3, "Test case 'aab' failed"

def test_case_aaa():
    assert countAnagrams("aaa") == 1, "Test case 'aaa' failed"