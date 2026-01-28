from solution import *

def test_example_1():
    assert maxProfit([1,2,3,0,2]) == 3, "Failed on example with multiple transactions and cooldown"

def test_example_2():
    assert maxProfit([1]) == 0, "Failed on single-day edge case"

def test_case_3():
    assert maxProfit([3, 1, 2]) == 1, "Failed on small cooldown scenario"