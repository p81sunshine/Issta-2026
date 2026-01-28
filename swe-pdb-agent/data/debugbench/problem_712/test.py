from solution import *

def test_example_1():
    baseCosts = [1, 7]
    toppingCosts = [3, 4]
    target = 10
    assert closestCost(baseCosts, toppingCosts, target) == 10

def test_example_2():
    baseCosts = [2, 3]
    toppingCosts = [4, 5, 100]
    target = 18
    assert closestCost(baseCosts, toppingCosts, target) == 17

def test_example_3():
    baseCosts = [3, 10]
    toppingCosts = [2, 5]
    target = 9
    assert closestCost(baseCosts, toppingCosts, target) == 8

def test_edge_case_double_topping():
    baseCosts = [0]
    toppingCosts = [3]
    target = 6
    assert closestCost(baseCosts, toppingCosts, target) == 6

def test_edge_case_two_toppings():
    baseCosts = [0]
    toppingCosts = [2, 2]
    target = 4
    assert closestCost(baseCosts, toppingCosts, target) == 4