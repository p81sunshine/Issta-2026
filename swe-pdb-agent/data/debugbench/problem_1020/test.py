from solution import *

def test_example_1():
    n = 4
    edges = [[0,1],[1,2],[1,3]]
    price = [2,2,10,6]
    trips = [[0,3],[2,1],[2,3]]
    expected = 23
    assert minimumTotalPrice(n, edges, price, trips) == expected, "Example 1 failed"

def test_example_2():
    n = 2
    edges = [[0,1]]
    price = [2,2]
    trips = [[0,0]]
    expected = 1
    assert minimumTotalPrice(n, edges, price, trips) == expected, "Example 2 failed"

def test_case_3():
    n = 3
    edges = [[0,1],[1,2]]
    price = [2,2,2]
    trips = [[0,2]]
    expected = 4
    assert minimumTotalPrice(n, edges, price, trips) == expected, "Case 3 failed"

def test_case_4():
    n = 2
    edges = [[0,1]]
    price = [2,2]
    trips = [[1,0]]
    expected = 3
    assert minimumTotalPrice(n, edges, price, trips) == expected, "Case 4 failed"