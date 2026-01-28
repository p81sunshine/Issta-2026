from solution import *

def test_example_1():
    assert closestCost([1,7], [3,4], 10) == 10

def test_example_2():
    assert closestCost([2,3], [4,5,100], 18) == 17

def test_example_3():
    assert closestCost([3,10], [2,5], 9) == 8

def test_keyword_arguments():
    assert closestCost(baseCosts=[1,7], toppingCosts=[3,4], target=10) == 10