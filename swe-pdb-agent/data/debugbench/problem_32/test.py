from solution import *

def test_example_1():
    pizza = ["A..","AAA","..."]
    k = 3
    assert ways(pizza, k) == 3, "Failed for first example with variable shadowing bug"

def test_example_2():
    pizza = ["A..","AA.","..."]
    k = 3
    assert ways(pizza, k) == 1, "Failed for second example with edge case"

def test_example_3():
    pizza = ["A..","A..","..."]
    k = 1
    assert ways(pizza, k) == 1, "Failed for base case k=1"

def test_insufficient_apples():
    pizza = ["A..", ".A."]
    k = 3
    assert ways(pizza, k) == 0, "Failed when total apples < k"