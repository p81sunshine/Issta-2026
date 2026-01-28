from solution import *

def test_example_1():
    assert totalMoney(4) == 10, "Example 1 failed"

def test_example_2():
    assert totalMoney(10) == 37, "Example 2 failed"

def test_example_3():
    assert totalMoney(20) == 96, "Example 3 failed"

def test_additional_case():
    assert totalMoney(8) == 30, "Additional case n=8 failed"