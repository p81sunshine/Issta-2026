from solution import *

def test_example_1():
    stations = [1,2,4,5,0]
    r = 1
    k = 2
    expected = 5
    assert maxPower(stations, r, k) == expected, "Example 1 failed"

def test_example_2():
    stations = [4,4,4,4]
    r = 0
    k = 3
    expected = 4
    assert maxPower(stations, r, k) == expected, "Example 2 failed"

def test_case_3():
    stations = [1]
    r = 0
    k = 1
    expected = 2
    assert maxPower(stations, r, k) == expected, "Test case 3 failed"

def test_edge_case():
    stations = [3,1,5]
    r = 0
    k = 0
    expected = 1
    assert maxPower(stations, r, k) == expected, "Edge case failed"