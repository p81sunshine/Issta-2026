from solution import *

def test_example_1():
    assert numberOfArithmeticSlices([2,4,6,8,10]) == 7, "Example 1 failed"

def test_example_2():
    assert numberOfArithmeticSlices([7,7,7,7,7]) == 16, "Example 2 failed"

def test_small_input():
    assert numberOfArithmeticSlices([1,2]) == 0, "Small input failed"

def test_three_elements():
    assert numberOfArithmeticSlices([1,2,3]) == 1, "Three elements test failed"

def test_four_elements():
    assert numberOfArithmeticSlices([1,3,5,7]) == 3, "Four elements test failed"