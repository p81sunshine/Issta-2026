from solution import *

def test_example_1():
    arr1 = [1,2,3,4]
    arr2 = [-1,4,5,6]
    assert maxAbsValExpr(arr1, arr2) == 13, "Example 1 failed"

def test_example_2():
    arr1 = [1,-2,-5,0,10]
    arr2 = [0,-2,-1,-7,-4]
    assert maxAbsValExpr(arr1, arr2) == 20, "Example 2 failed"

def test_all_zeros():
    arr1 = [0, 0]
    arr2 = [0, 0]
    assert maxAbsValExpr(arr1, arr2) == 1, "All zeros case failed"

def test_val2_max():
    arr1 = [0, 5]
    arr2 = [5, 0]
    assert maxAbsValExpr(arr1, arr2) == 11, "Val2 max case failed"

def test_val3_val4_max():
    arr1 = [3, 0]
    arr2 = [0, 0]
    assert maxAbsValExpr(arr1, arr2) == 4, "Val3/Val4 max case failed"