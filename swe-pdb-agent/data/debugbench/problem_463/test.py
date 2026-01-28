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

def test_insufficient_apples():
    pizza = ["A..","...","..."]
    k = 2
    assert ways(pizza, k) == 0, "Insufficient apples case failed"

def test_sufficient_apples():
    pizza = ["A.", ".A"]
    k = 2
    assert ways(pizza, k) == 2, "Sufficient apples but buggy code returns 0"