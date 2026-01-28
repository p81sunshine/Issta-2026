from solution import *

def test_example_1():
    lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
    expected = "abab"
    assert find_the_string(lcp) == expected, "Failed for example 1"

def test_example_2():
    lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
    expected = "aaaa"
    assert find_the_string(lcp) == expected, "Failed for example 2"

def test_example_3():
    lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
    expected = ""
    assert find_the_string(lcp) == expected, "Failed for example 3"

def test_n1_valid():
    lcp = [[1]]
    expected = "a"
    assert find_the_string(lcp) == expected, "Failed for single character valid case"

def test_n1_invalid():
    lcp = [[0]]
    expected = ""
    assert find_the_string(lcp) == expected, "Failed for single character invalid case"

def test_too_many_distinct():
    n = 27
    lcp = [[0]*n for _ in range(n)]
    for i in range(n):
        lcp[i][i] = n - i
    expected = ""
    assert find_the_string(lcp) == expected, "Failed for case requiring more than 26 distinct characters"