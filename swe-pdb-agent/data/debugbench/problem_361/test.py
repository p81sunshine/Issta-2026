from solution import *

def test_example_1():
    assert minimumTime([1,2,3], 5) == 3, "Example 1 failed"

def test_example_2():
    assert minimumTime([2], 1) == 2, "Example 2 failed"

def test_case_multiple_buses_needed():
    assert minimumTime([5, 10], 2) == 10, "Test case where multiple buses contribute to total trips failed"

def test_case_higher_totaltrips():
    assert minimumTime([1, 1], 3) == 2, "Test case with higher total trips than number of buses failed"