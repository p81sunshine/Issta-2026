from solution import *

def test_example_1():
    plants = [2,2,3,3]
    capacityA = 5
    capacityB = 5
    expected = 1
    actual = minimumRefill(plants, capacityA, capacityB)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_example_2():
    plants = [2,2,3,3]
    capacityA = 3
    capacityB = 4
    expected = 2
    actual = minimumRefill(plants, capacityA, capacityB)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_example_3():
    plants = [5]
    capacityA = 10
    capacityB = 8
    expected = 0
    actual = minimumRefill(plants, capacityA, capacityB)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_edge_case_middle():
    plants = [1,3,1]
    capacityA = 3
    capacityB = 3
    expected = 1
    actual = minimumRefill(plants, capacityA, capacityB)
    assert actual == expected, f"Expected {expected}, got {actual}"