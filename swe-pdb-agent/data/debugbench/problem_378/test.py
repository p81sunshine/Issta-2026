from solution import *

def test_example_1():
    words = ["abcd","dcba","lls","s","sssll"]
    expected = [[0,1],[1,0],[3,2],[2,4]]
    result = palindromePairs(words)
    assert sorted(result) == sorted(expected), "Example 1 failed"

def test_example_2():
    words = ["bat","tab","cat"]
    expected = [[0,1],[1,0]]
    result = palindromePairs(words)
    assert sorted(result) == sorted(expected), "Example 2 failed"

def test_example_3():
    words = ["a",""]
    expected = [[0,1],[1,0]]
    result = palindromePairs(words)
    assert sorted(result) == sorted(expected), "Example 3 failed"