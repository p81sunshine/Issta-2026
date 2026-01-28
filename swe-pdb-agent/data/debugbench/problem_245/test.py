from solution import *

def test_example_1():
    n = 8
    edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    expected = [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
    result = getAncestors(n, edges)
    assert result == expected, "Example 1 failed"

def test_example_2():
    n = 5
    edges = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    expected = [[], [0], [0,1], [0,1,2], [0,1,2,3]]
    result = getAncestors(n, edges)
    assert result == expected, "Example 2 failed"

def test_edge_case_1():
    n = 1
    edges = []
    expected = [[]]
    result = getAncestors(n, edges)
    assert result == expected, "Edge case n=1 failed"

def test_edge_case_2():
    n = 2
    edges = [[0,1]]
    expected = [[], [0]]
    result = getAncestors(n, edges)
    assert result == expected, "Edge case n=2 with one edge failed"

def test_multiple_parents():
    n = 3
    edges = [[0,2], [1,2]]
    expected = [[], [], [0, 1]]
    result = getAncestors(n, edges)
    assert result == expected, "Test case with multiple parents failed"

def test_deep_ancestors():
    n = 4
    edges = [[0,1], [1,2], [0,3], [1,3], [2,3]]
    expected = [[], [0], [0,1], [0,1,2]]
    result = getAncestors(n, edges)
    assert result == expected, "Test case for deep ancestors failed"