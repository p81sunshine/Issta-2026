from solution import *

def test_example_1():
    assert minimum_total_cost([1,2,3,4,5], [1,2,3,4,5]) == 10

def test_example_2():
    assert minimum_total_cost([2,2,2,1,3], [1,2,2,3,3]) == 10

def test_example_3():
    assert minimum_total_cost([1,2,2], [1,2,2]) == -1

def test_edge_case_all_equal():
    assert minimum_total_cost([1,1], [1,1]) == -1

def test_already_valid():
    assert minimum_total_cost([1,2], [2,1]) == 0