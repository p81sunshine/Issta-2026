from solution import *

def test_example_1():
    n = 5
    edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
    assert isPossible(n, edges) == True, "Example 1 should return True"

def test_example_2():
    n = 4
    edges = [[1,2],[3,4]]
    assert isPossible(n, edges) == True, "Example 2 should return True"

def test_example_3():
    n = 4
    edges = [[1,2],[1,3],[1,4]]
    assert isPossible(n, edges) == False, "Example 3 should return False"

def test_two_odd_connected_with_third_node():
    n = 3
    edges = [[1,2]]
    assert isPossible(n, edges) == True, "Two connected odd-degree nodes with third node should return True"

def test_four_odd_complete_graph():
    n = 4
    edges = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    assert isPossible(n, edges) == False, "Complete graph with 4 nodes (all odd degrees) should return False"