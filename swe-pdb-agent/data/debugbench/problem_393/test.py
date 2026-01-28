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

def test_case_4():
    pizza = ["A..","A..","A.."]
    k = 2
    assert ways(pizza, k) == 2, "Test case 4 failed"

def test_case_5():
    pizza = ["A.A","A.A"]
    k = 2
    assert ways(pizza, k) == 3, "Test case 5 failed"