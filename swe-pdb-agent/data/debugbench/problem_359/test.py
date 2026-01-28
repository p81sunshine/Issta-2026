from solution import *

def test_example_1():
    lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
    assert findTheString(lcp) == "abab", "Example 1 should return 'abab'"

def test_example_2():
    lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
    assert findTheString(lcp) == "aaaa", "Example 2 should return 'aaaa'"

def test_example_3():
    lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
    assert findTheString(lcp) == "", "Example 3 should return empty string"

def test_single_char_valid():
    lcp = [[1]]
    assert findTheString(lcp) == "a", "Single character 'a' should be valid"

def test_buggy_symmetric_case():
    lcp = [[2,1],[1,1]]
    assert findTheString(lcp) == "aa", "Valid symmetric LCP should return 'aa'"