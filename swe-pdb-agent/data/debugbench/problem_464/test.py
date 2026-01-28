from solution import *

def test_example_1():
    lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
    assert findTheString(lcp) == "abab", "Failed for case with alternating letters"

def test_example_2():
    lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
    assert findTheString(lcp) == "aaaa", "Failed for single-letter string case"

def test_example_3():
    lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
    assert findTheString(lcp) == "", "Failed for invalid diagonal value case"

def test_pattern_lcp_bug():
    lcp = [[2,1],[1,1]]
    assert findTheString(lcp) == "aa", "Failed for pattern_lcp calculation error case"