from solution import *

def test_example_1():
    pizza = ["A..","AAA","..."]
    k = 3
    expected = 3
    assert ways(pizza, k) == expected, f"Expected {expected} ways for example 1"

def test_example_2():
    pizza = ["A..","AA.","..."]
    k = 3
    expected = 1
    assert ways(pizza, k) == expected, f"Expected {expected} ways for example 2"

def test_example_3():
    pizza = ["A..","A..","..."]
    k = 1
    expected = 1
    assert ways(pizza, k) == expected, f"Expected {expected} ways for example 3"

def test_single_row_cut():
    pizza = ["AA"]
    k = 2
    expected = 1
    assert ways(pizza, k) == expected, f"Expected {expected} ways for single row cut case"