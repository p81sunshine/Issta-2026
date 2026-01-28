from solution import *

def test_example_1():
    pizza = ["A..", "AAA", "..."]
    k = 3
    assert ways(pizza, k) == 3, "Example 1 should return 3"

def test_example_2():
    pizza = ["A..", "AA.", "..."]
    k = 3
    assert ways(pizza, k) == 1, "Example 2 should return 1"

def test_example_3():
    pizza = ["A..", "A..", "..."]
    k = 1
    assert ways(pizza, k) == 1, "Example 3 should return 1"

def test_edge_no_apples():
    pizza = ["...", "...", "..."]
    k = 1
    assert ways(pizza, k) == 0, "No apples should return 0"

def test_edge_single_cell():
    pizza = ["A"]
    k = 1
    assert ways(pizza, k) == 1, "Single cell with apple should return 1"