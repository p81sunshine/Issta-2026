from solution import *

def test_example_1():
    assert maxProfit([7,1,5,3,6,4]) == 7, "Example 1 failed"

def test_example_2():
    assert maxProfit([1,2,3,4,5]) == 4, "Example 2 failed"

def test_edge_case_1():
    assert maxProfit([2,1,2]) == 1, "Edge case 1 failed"

def test_edge_case_2():
    assert maxProfit([2,4,1,2]) == 3, "Edge case 2 failed"

def test_no_profit():
    assert maxProfit([7,6,4,3,1]) == 0, "No profit case failed"