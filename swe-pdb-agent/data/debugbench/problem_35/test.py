from solution import *

def test_example_1():
    words = ["abcd","dcba","lls","s","sssll"]
    expected = [[0,1],[1,0],[3,2],[2,4]]
    assert palindrome_pairs(words) == expected, "Failed for example 1"

def test_example_2():
    words = ["bat","tab","cat"]
    expected = [[0,1],[1,0]]
    assert palindrome_pairs(words) == expected, "Failed for example 2"

def test_example_3():
    words = ["a",""]
    expected = [[0,1],[1,0]]
    assert palindrome_pairs(words) == expected, "Failed for example 3"

def test_edge_case_empty():
    words = []
    expected = []
    assert palindrome_pairs(words) == expected, "Failed for empty input"

def test_edge_case_single_word():
    words = ["a"]
    expected = []
    assert palindrome_pairs(words) == expected, "Failed for single word input"