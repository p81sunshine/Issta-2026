from solution import *

def test_example_1():
    assert minimumTime([1,2,3], 5) == 3, "Example 1 failed"

def test_example_2():
    assert minimumTime([2], 1) == 2, "Example 2 failed"

def test_single_bus_multiple_trips():
    assert minimumTime([5], 3) == 15, "Single bus with multiple trips failed"

def test_two_buses_total_2():
    assert minimumTime([5,10], 2) == 10, "Two buses with total 2 trips failed"

def test_multiple_buses_exact_sum():
    assert minimumTime([2,3], 4) == 6, "Multiple buses requiring exact sum failed"