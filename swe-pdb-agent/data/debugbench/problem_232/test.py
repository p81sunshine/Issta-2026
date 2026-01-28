from solution import *

def test_example_1():
    assert closest_cost([1,7], [3,4], 10) == 10, "Example 1 failed"

def test_example_2():
    assert closest_cost([2,3], [4,5,100], 18) == 17, "Example 2 failed"

def test_example_3():
    assert closest_cost([3,10], [2,5], 9) == 8, "Example 3 failed"

def test_tie_between_lower_and_higher():
    assert closest_cost([5], [4], 7) == 5, "Tie case should select lower value"