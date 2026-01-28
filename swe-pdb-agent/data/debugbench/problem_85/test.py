from solution import *

def test_example_1():
    assert isPossible(5, [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]) == True

def test_example_2():
    assert isPossible(4, [[1,2],[3,4]]) == True

def test_example_3():
    assert isPossible(4, [[1,2],[1,3],[1,4]]) == False

def test_zero_odd_degrees():
    n = 3
    edges = [[1,2], [1,3], [2,3]]  # All even degrees
    assert isPossible(n, edges) == True

def test_two_nodes_connected():
    assert isPossible(2, [[1,2]]) == False