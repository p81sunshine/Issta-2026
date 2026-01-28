from solution import *

def test_example_1():
    pizza = ["A..","AAA","..."]
    k = 3
    assert ways(pizza, k) == 3, "Test case 1 failed"

def test_example_2():
    pizza = ["A..","AA.","..."]
    k = 3
    assert ways(pizza, k) == 1, "Test case 2 failed"

def test_example_3():
    pizza = ["A..","A..","..."]
    k = 1
    assert ways(pizza, k) == 1, "Test case 3 failed"

def test_insufficient_apples():
    pizza = ["A..", "..."]
    k = 3
    assert ways(pizza, k) == 0, "Test insufficient apples failed"