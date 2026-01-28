from solution import *

def test_example_1():
    assert minimumTime([1,2,3], 5) == 3, "Test case 1 failed"

def test_example_2():
    assert minimumTime([2], 1) == 2, "Test case 2 failed"

def test_edge_case_multiple_buses():
    assert minimumTime([5,5,5], 3) == 5, "Edge case with multiple buses failed"

def test_edge_case_two_buses():
    assert minimumTime([2,3], 2) == 3, "Edge case two buses failed"

def test_single_bus_sufficient():
    assert minimumTime([1, 100], 2) == 2, "Single bus sufficient test failed"