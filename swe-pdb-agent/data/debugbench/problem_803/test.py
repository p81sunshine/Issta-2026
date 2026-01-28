from solution import *

def test_example_1():
    pizza = ["A..","AAA","..."]
    k = 3
    assert ways(pizza, k) == 3, "Example 1 failed"

def test_example_2():
    pizza = ["A..","AA.","..."]
    k = 3
    assert ways(pizza, k) == 1, "Example 2 failed"

def test_example_3():
    pizza = ["A..","A..","..."]
    k = 1
    assert ways(pizza, k) == 1, "Example 3 failed"

def test_simple_cut_case():
    pizza = ["AA"]
    k = 2
    assert ways(pizza, k) == 1, "Simple cut case failed"