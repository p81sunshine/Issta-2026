from solution import *

def test_example_1():
    baseCosts = [1, 7]
    toppingCosts = [3, 4]
    target = 10
    assert closestCost(baseCosts, toppingCosts, target) == 10, "Example 1 failed"

def test_example_2():
    baseCosts = [2, 3]
    toppingCosts = [4, 5, 100]
    target = 18
    assert closestCost(baseCosts, toppingCosts, target) == 17, "Example 2 failed"

def test_example_3():
    baseCosts = [3, 10]
    toppingCosts = [2, 5]
    target = 9
    assert closestCost(baseCosts, toppingCosts, target) == 8, "Example 3 failed"

def test_edge_case_exact_match():
    baseCosts = [5]
    toppingCosts = [0]
    target = 5
    assert closestCost(baseCosts, toppingCosts, target) == 5, "Exact match edge case failed"

def test_edge_case_multiple_toppings():
    baseCosts = [1]
    toppingCosts = [2, 3]
    target = 4
    assert closestCost(baseCosts, toppingCosts, target) == 4, "Multiple toppings edge case failed"