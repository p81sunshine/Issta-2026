from solution import *

def test_example_1():
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","o"]
    expected = ["facebook","google","leetcode"]
    assert wordSubsets(words1, words2) == expected, "Failed on example 1"

def test_example_2():
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["l","e"]
    expected = ["apple","google","leetcode"]
    assert wordSubsets(words1, words2) == expected, "Failed on example 2"

def test_max_counts():
    words1 = ["abbc", "aabbcc", "abc"]
    words2 = ["abc", "abbc"]
    expected = ["abbc", "aabbcc"]
    assert wordSubsets(words1, words2) == expected, "Failed on max count scenario"