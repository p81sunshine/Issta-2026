from solution import *

def test_example_1():
    baseCosts = [1, 7]
    toppingCosts = [3, 4]
    target = 10
    assert closestCost(baseCosts, toppingCosts, target) == 10, "Failed example 1"

def test_example_2():
    baseCosts = [2, 3]
    toppingCosts = [4, 5, 100]
    target = 18
    assert closestCost(baseCosts, toppingCosts, target) == 17, "Failed example 2"

def test_example_3():
    baseCosts = [3, 10]
    toppingCosts = [2, 5]
    target = 9
    assert closestCost(baseCosts, toppingCosts, target) == 8, "Failed example 3"

def test_edge_case_double_topping():
    baseCosts = [5]
    toppingCosts = [3]
    target = 11
    assert closestCost(baseCosts, toppingCosts, target) == 11, "Failed edge case with double topping usage"