from solution import *

def test_example_1():
    n = 8
    edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    expected = [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
    assert getAncestors(n, edges) == expected

def test_example_2():
    n = 5
    edges = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    expected = [[],[0],[0,1],[0,1,2],[0,1,2,3]]
    assert getAncestors(n, edges) == expected

def test_single_node():
    n = 1
    edges = []
    expected = [[]]
    assert getAncestors(n, edges) == expected

def test_linear_chain():
    n = 3
    edges = [[0,1], [1,2]]
    expected = [[], [0], [0,1]]
    assert getAncestors(n, edges) == expected