from solution import *

def test_example_1():
    n = 4
    edges = [[0,1],[1,2],[1,3]]
    price = [2,2,10,6]
    trips = [[0,3],[2,1],[2,3]]
    assert minimumTotalPrice(n, edges, price, trips) == 23, "Failed on example 1"

def test_example_2():
    n = 2
    edges = [[0,1]]
    price = [2,2]
    trips = [[0,0]]
    assert minimumTotalPrice(n, edges, price, trips) == 1, "Failed on example 2"

def test_single_node():
    n = 1
    edges = []
    price = [2]
    trips = [[0,0]]
    assert minimumTotalPrice(n, edges, price, trips) == 1, "Failed on single node case"

def test_same_node_trip():
    n = 3
    edges = [[0,1],[1,2]]
    price = [2,2,2]
    trips = [[2,2]]
    assert minimumTotalPrice(n, edges, price, trips) == 1, "Failed on same-node trip case"