from solution import *

def test_example_1():
    assert maxProfit([7,1,5,3,6,4]) == 7, "Failed for case with multiple transactions"

def test_example_2():
    assert maxProfit([1,2,3,4,5]) == 4, "Failed for strictly increasing prices"

def test_example_3():
    assert maxProfit([7,6,4,3,1]) == 0, "Failed for strictly decreasing prices"

def test_edge_case_empty():
    assert maxProfit([]) == 0, "Failed for empty input"

def test_edge_case_single_element():
    assert maxProfit([5]) == 0, "Failed for single-element input"

def test_overlapping_transactions():
    assert maxProfit([1,3,2,5]) == 5, "Failed to handle overlapping transactions properly"