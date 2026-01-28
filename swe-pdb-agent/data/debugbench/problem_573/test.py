from solution import *

def test_example_1():
    assert maxProfit([7,1,5,3,6,4]) == 7

def test_example_2():
    assert maxProfit([1,2,3,4,5]) == 4

def test_example_3():
    assert maxProfit([7,6,4,3,1]) == 0

def test_empty_prices():
    assert maxProfit([]) == 0

def test_single_price():
    assert maxProfit([5]) == 0

def test_two_prices_profit():
    assert maxProfit([1,2]) == 1

def test_two_prices_loss():
    assert maxProfit([2,1]) == 0