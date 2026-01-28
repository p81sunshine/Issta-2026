from solution import *

def test_example_1():
    lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
    assert findTheString(lcp) == "abab"

def test_example_2():
    lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
    assert findTheString(lcp) == "aaaa"

def test_example_3():
    lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
    assert findTheString(lcp) == ""

def test_case_27_letters():
    n = 27
    lcp = [[0]*n for _ in range(n)]
    for i in range(n):
        lcp[i][i] = n - i
    assert findTheString(lcp) == ""

def test_case_n1():
    lcp = [[1]]
    assert findTheString(lcp) == "a"