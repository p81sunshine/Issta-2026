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

def test_not_enough_apples():
    pizza = ["A"]
    k = 2
    assert ways(pizza, k) == 0, "Not enough apples case failed"

def test_no_apples_case():
    pizza = ["..."]
    k = 1
    assert ways(pizza, k) == 0, "No apples case failed"