from solution import *

def test_example_1():
    assert closest_cost([1,7], [3,4], 10) == 10, "Example 1 failed"

def test_example_2():
    assert closest_cost([2,3], [4,5,100], 18) == 17, "Example 2 failed"

def test_example_3():
    assert closest_cost([3,10], [2,5], 9) == 8, "Example 3 failed"

def test_edge_case_exact_base():
    assert closest_cost([10], [1,2], 10) == 10, "Edge case: exact base cost failed"

def test_edge_case_no_toppings():
    assert closest_cost([5], [10,20], 7) == 5, "Edge case: no toppings selected failed"