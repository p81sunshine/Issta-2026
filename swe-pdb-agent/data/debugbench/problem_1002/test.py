from solution import *

def test_example_1():
    lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
    assert findTheString(lcp) == "abab", "Failed for example 1"

def test_example_2():
    lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
    assert findTheString(lcp) == "aaaa", "Failed for example 2"

def test_example_3():
    lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
    assert findTheString(lcp) == "", "Failed for example 3"

def test_single_character():
    lcp = [[1]]
    assert findTheString(lcp) == "a", "Failed for single character case"

def test_invalid_lcp():
    lcp = [[2, 0], [0, 2]]
    assert findTheString(lcp) == "", "Failed for invalid diagonal value"