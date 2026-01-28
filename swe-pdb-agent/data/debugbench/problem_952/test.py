from solution import *

def test_example_1():
    startWords = ["ant","act","tack"]
    targetWords = ["tack","act","acti"]
    assert wordCount(startWords, targetWords) == 2, "Example 1 failed"

def test_example_2():
    startWords = ["ab","a"]
    targetWords = ["abc","abcd"]
    assert wordCount(startWords, targetWords) == 1, "Example 2 failed"

def test_edge_case():
    startWords = ["a"]
    targetWords = ["aa"]
    assert wordCount(startWords, targetWords) == 1, "Edge case failed"