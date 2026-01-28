from solution import *

def test_example_1():
    n = 4
    edges = [[0,1],[1,2],[1,3]]
    price = [2,2,10,6]
    trips = [[0,3],[2,1],[2,3]]
    assert minimumTotalPrice(n, edges, price, trips) == 23, "Test case 1 failed"

def test_example_2():
    n = 2
    edges = [[0,1]]
    price = [2,2]
    trips = [[0,0]]
    assert minimumTotalPrice(n, edges, price, trips) == 1, "Test case 2 failed"

def test_single_node_trip():
    n = 1
    edges = []
    price = [10]
    trips = [[0,0]]
    assert minimumTotalPrice(n, edges, price, trips) == 5, "Single node trip test failed"