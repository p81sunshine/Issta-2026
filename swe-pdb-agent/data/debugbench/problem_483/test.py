from solution import *

def test_example_1():
    assert numberOfArithmeticSlices([2,4,6,8,10]) == 7, "Example 1 failed"

def test_example_2():
    assert numberOfArithmeticSlices([7,7,7,7,7]) == 16, "Example 2 failed"

def test_case_overlap():
    assert numberOfArithmeticSlices([0,2,2,4,6]) == 6, "Overlap case failed"

def test_edge_case():
    assert numberOfArithmeticSlices([0,0,0]) == 1, "Edge case failed"