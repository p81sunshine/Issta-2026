from solution import *

def test_example_1():
    pizza = ["A..","AAA","..."]
    k = 3
    assert ways(pizza, k) == 3, "Failed for example 1: 3 ways expected"

def test_example_2():
    pizza = ["A..","AA.","..."]
    k = 3
    assert ways(pizza, k) == 1, "Failed for example 2: 1 way expected"

def test_example_3():
    pizza = ["A..","A..","..."]
    k = 1
    assert ways(pizza, k) == 1, "Failed for example 3: 1 way expected"

def test_edge_case_single_apple():
    pizza = ["A"]
    k = 1
    assert ways(pizza, k) == 1, "Failed for edge case: single apple pizza"