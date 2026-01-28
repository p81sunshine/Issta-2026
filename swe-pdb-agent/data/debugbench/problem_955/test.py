from solution import *

def test_example_1():
    n = 4
    edges = [[0,1],[1,2],[1,3]]
    price = [2,2,10,6]
    trips = [[0,3],[2,1],[2,3]]
    expected = 23
    actual = minimumTotalPrice(n, edges, price, trips)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_example_2():
    n = 2
    edges = [[0,1]]
    price = [2,2]
    trips = [[0,0]]
    expected = 1
    actual = minimumTotalPrice(n, edges, price, trips)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_single_node():
    n = 1
    edges = []
    price = [4]
    trips = [[0,0]]
    expected = 2
    actual = minimumTotalPrice(n, edges, price, trips)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_two_node_path():
    n = 2
    edges = [[0,1]]
    price = [4,4]
    trips = [[0,1]]
    expected = 6
    actual = minimumTotalPrice(n, edges, price, trips)
    assert actual == expected, f"Expected {expected}, got {actual}"