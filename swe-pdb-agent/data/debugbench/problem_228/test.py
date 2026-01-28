from solution import *

def test_example_1():
    assert maxProfit([7,1,5,3,6,4]) == 7

def test_example_2():
    assert maxProfit([1,2,3,4,5]) == 4

def test_example_3():
    assert maxProfit([7,6,4,3,1]) == 0

def test_custom_case():
    assert maxProfit([3,2,6,5,0,3]) == 7

def test_edge_empty():
    assert maxProfit([]) == 0

def test_edge_single():
    assert maxProfit([5]) == 0