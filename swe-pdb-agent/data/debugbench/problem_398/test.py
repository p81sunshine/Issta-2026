from solution import *

def test_example_1():
    n = 4
    edges = [[0,1],[1,2],[1,3]]
    price = [2,2,10,6]
    trips = [[0,3],[2,1],[2,3]]
    assert minimum_total_price(n, edges, price, trips) == 23

def test_example_2():
    n = 2
    edges = [[0,1]]
    price = [2,2]
    trips = [[0,0]]
    assert minimum_total_price(n, edges, price, trips) == 1

def test_trip_to_parent():
    n = 3
    edges = [[0,1],[1,2]]
    price = [2,2,2]
    trips = [[2,1]]
    assert minimum_total_price(n, edges, price, trips) == 3