from solution import *

def test_example_1():
    assert minimumTime([1,2,3], 5) == 3, "Failed for example 1"

def test_example_2():
    assert minimumTime([2], 1) == 2, "Failed for example 2"

def test_case_2_3_2():
    assert minimumTime([2,3], 2) == 3, "Failed for [2,3] with 2 trips"

def test_same_times():
    assert minimumTime([5,5,5], 3) == 5, "Failed for same time values"

def test_multiple_trips_per_bus():
    assert minimumTime([1,2], 3) == 2, "Failed for multiple trips per bus scenario"