from solution import *

def test_example_1():
    assert minimumTime([1,2,3], 5) == 3, "Example 1 failed"

def test_example_2():
    assert minimumTime([2], 1) == 2, "Example 2 failed"

def test_single_bus_multiple_trips():
    assert minimumTime([2], 3) == 6, "Single bus multiple trips failed"

def test_two_buses_same_time():
    assert minimumTime([3,3], 2) == 3, "Two buses same time failed"

def test_multiple_buses_combined_trips():
    assert minimumTime([5,10,15], 3) == 10, "Combined trips calculation failed"