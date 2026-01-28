from solution import *

def test_example_1():
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    assert arrayStringsAreEqual(word1, word2) is True, "Should return True as both concatenate to 'abc'"

def test_example_2():
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    assert arrayStringsAreEqual(word1, word2) is False, "Should return False as 'acb' != 'abc'"

def test_example_3():
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    assert arrayStringsAreEqual(word1, word2) is True, "Should return True as both concatenate to 'abcddefg'"

def test_reversed_order():
    word1 = ["a", "b"]
    word2 = ["ab"]
    assert arrayStringsAreEqual(word1, word2) is True, "Should return True when order is not reversed"