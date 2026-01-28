from solution import *

def test_example_1():
    assert maxPower([1,2,4,5,0], 1, 2) == 5, "Example 1 failed"

def test_example_2():
    assert maxPower([4,4,4,4], 0, 3) == 4, "Example 2 failed"

def test_r_zero_case():
    assert maxPower([1,1], 0, 1) == 1, "r=0 case failed"

def test_k_zero_case():
    assert maxPower([5,5,5], 1, 0) == 10, "k=0 case failed"

def test_single_station():
    assert maxPower([1], 0, 0) == 1, "Single station case failed"