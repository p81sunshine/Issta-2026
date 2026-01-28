from solution import *

def test_example_1():
    assert maxAbsValExpr([1,2,3,4], [-1,4,5,6]) == 13, "Example 1 failed"

def test_example_2():
    assert maxAbsValExpr([1,-2,-5,0,10], [0,-2,-1,-7,-4]) == 20, "Example 2 failed"

def test_val4_case():
    assert maxAbsValExpr([0, -7], [0, -7]) == 15, "Val4 case failed"

def test_single_element():
    assert maxAbsValExpr([5], [3]) == 0, "Single element case failed"