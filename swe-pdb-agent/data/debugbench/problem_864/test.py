from solution import *

def test_example_1():
    assert minimumTotalPrice(4, [[0,1],[1,2],[1,3]], [2,2,10,6], [[0,3],[2,1],[2,3]]) == 23

def test_example_2():
    assert minimumTotalPrice(2, [[0,1]], [2,2], [[0,0]]) == 1

def test_single_node_trip():
    assert minimumTotalPrice(1, [], [2], [[0,0]]) == 1