from solution import *

def test_example_1():
    roads = [[0,1],[0,2],[0,3]]
    seats = 5
    assert minimumFuelCost(roads, seats) == 3, "Example 1 should return 3"

def test_example_2():
    roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
    seats = 2
    assert minimumFuelCost(roads, seats) == 7, "Example 2 should return 7"

def test_example_3():
    roads = []
    seats = 1
    assert minimumFuelCost(roads, seats) == 0, "Example 3 should return 0"

def test_single_node_case():
    roads = [[0,1]]
    seats = 3
    assert minimumFuelCost(roads, seats) == 1, "Single node case should return 1"