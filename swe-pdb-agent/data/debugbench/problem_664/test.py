from solution import *

def test_example_1():
    arr1 = [1,2,3,4]
    arr2 = [-1,4,5,6]
    assert maxAbsValExpr(arr1, arr2) == 13, "Example 1 should return 13"

def test_example_2():
    arr1 = [1,-2,-5,0,10]
    arr2 = [0,-2,-1,-7,-4]
    assert maxAbsValExpr(arr1, arr2) == 20, "Example 2 should return 20"

def test_single_element():
    arr1 = [5]
    arr2 = [3]
    assert maxAbsValExpr(arr1, arr2) == 0, "Single element case should return 0"

def test_all_zeros():
    arr1 = [0, 0]
    arr2 = [0, 0]
    assert maxAbsValExpr(arr1, arr2) == 1, "All zeros with length 2 should return 1"

def test_val4_max():
    arr1 = [3, 1]
    arr2 = [2, -1]
    assert maxAbsValExpr(arr1, arr2) == 6, "Test case where val4 produces maximum difference"