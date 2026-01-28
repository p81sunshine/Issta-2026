from solution import *

def test_example_1():
    roads = [[0,1],[0,2],[0,3]]
    seats = 5
    assert minimumFuelCost(roads, seats) == 3, "Example 1 failed"

def test_example_2():
    roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
    seats = 2
    assert minimumFuelCost(roads, seats) == 7, "Example 2 failed"

def test_example_3():
    roads = []
    seats = 1
    assert minimumFuelCost(roads, seats) == 0, "Example 3 failed"

def test_edge_case_multiple_levels():
    roads = [[0,1],[1,2],[2,3]]
    seats = 3
    assert minimumFuelCost(roads, seats) == 3, "Multi-level tree calculation failed"