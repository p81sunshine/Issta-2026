from solution import *

def test_example_1():
    assert pivotArray([9,12,5,10,14,3,10], 10) == [9,5,3,10,10,12,14], "Failed on example 1"

def test_example_2():
    assert pivotArray([-3,4,3,2], 2) == [-3,2,4,3], "Failed on example 2"

def test_mixed_order():
    assert pivotArray([3,1,4,2], 3) == [1,2,3,4], "Failed on mixed order case"

def test_all_equal():
    assert pivotArray([5,5,5], 5) == [5,5,5], "Failed on all equal elements"

def test_all_less():
    assert pivotArray([1,2,3], 4) == [1,2,3], "Failed on all elements less than pivot"