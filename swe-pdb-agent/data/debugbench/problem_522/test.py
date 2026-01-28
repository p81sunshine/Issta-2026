from solution import *

def test_example_1():
    assert maxAbsValExpr([1,2,3,4], [-1,4,5,6]) == 13, "Example 1 failed"

def test_example_2():
    assert maxAbsValExpr([1,-2,-5,0,10], [0,-2,-1,-7,-4]) == 20, "Example 2 failed"

def test_two_element_case():
    assert maxAbsValExpr([1,3], [2,-1]) == 6, "Two-element case failed"

def test_all_same_elements():
    assert maxAbsValExpr([5,5], [5,5]) == 1, "All same elements case failed"

def test_val2_max_case():
    assert maxAbsValExpr([0,4], [3,0]) == 8, "Val2 max case failed"