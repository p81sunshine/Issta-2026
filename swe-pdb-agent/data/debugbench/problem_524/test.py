from solution import *

def test_example_1():
    lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
    assert findTheString(lcp) == "abab", "First example should return 'abab'"

def test_example_2():
    lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
    assert findTheString(lcp) == "aaaa", "Second example should return 'aaaa'"

def test_example_3():
    lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
    assert findTheString(lcp) == "", "Third example should return empty string"

def test_max_26_letters():
    n = 27
    lcp = [[n - i if i == j else 0 for j in range(n)] for i in range(n)]
    assert findTheString(lcp) == "", "Should return empty when more than 26 letters are needed"

def test_edge_case_n1():
    assert findTheString([[1]]) == 'a', "n=1 should return 'a'"