from solution import *

def test_example_1():
    assert findLongestWord("abpcplea", ["ale","apple","monkey","plea"]) == "apple", "Example 1 failed"

def test_example_2():
    assert findLongestWord("abpcplea", ["a","b","c"]) == "a", "Example 2 failed"

def test_invalid_subsequence():
    assert findLongestWord("ab", ["aba"]) == "", "Test invalid subsequence (aba in ab) failed"

def test_same_length_lex_order():
    assert findLongestWord("abcd", ["zbc", "abc"]) == "abc", "Test lex order for same length words failed"

def test_no_valid_word():
    assert findLongestWord("abc", ["def", "ghi"]) == "", "Test no valid subsequence failed"