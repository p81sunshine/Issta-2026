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

def test_no_apples():
    pizza = ["...","..."]
    k = 1
    assert ways(pizza, k) == 0, "No apples case failed"

def test_single_cell():
    pizza = ["A"]
    k = 1
    assert ways(pizza, k) == 1, "Single cell with apple"

def test_insufficient_apples():
    pizza = ["A..", "A..", "..."]
    k = 3  # Total apples are 2, so output should be 0
    assert ways(pizza, k) == 0, "Insufficient apples case failed"