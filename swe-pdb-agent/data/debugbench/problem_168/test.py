from solution import *

def test_example_1():
    n = 5
    edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
    assert is_possible(n, edges) is True, "Test case 1 failed"

def test_example_2():
    n = 4
    edges = [[1,2],[3,4]]
    assert is_possible(n, edges) is True, "Test case 2 failed"

def test_example_3():
    n = 4
    edges = [[1,2],[1,3],[1,4]]
    assert is_possible(n, edges) is False, "Test case 3 failed"

def test_two_connected_odd_nodes():
    n = 4
    edges = [[1,2],[2,3],[3,4],[4,1],[1,3]]
    assert is_possible(n, edges) is False, "Test case for connected odd-degree nodes failed"

def test_two_nodes_connected():
    n = 2
    edges = [[1,2]]
    assert is_possible(n, edges) is False, "Test case for two connected nodes failed"