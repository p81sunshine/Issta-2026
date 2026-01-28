from solution import *

def test_example_1():
    arr1 = [1,2,3,4]
    arr2 = [-1,4,5,6]
    expected = 13
    assert maxAbsValExpr(arr1, arr2) == expected, "Example 1 failed"

def test_example_2():
    arr1 = [1,-2,-5,0,10]
    arr2 = [0,-2,-1,-7,-4]
    expected = 20
    assert maxAbsValExpr(arr1, arr2) == expected, "Example 2 failed"

def test_edge_case_two_zeros():
    arr1 = [0,0]
    arr2 = [0,0]
    expected = 1
    assert maxAbsValExpr(arr1, arr2) == expected, "Edge case with zeros failed"

def test_case_single_max():
    arr1 = [0,1]
    arr2 = [0,1]
    expected = 3
    assert maxAbsValExpr(arr1, arr2) == expected, "Single max case failed"

def test_max_from_val2():
    arr1 = [0,0]
    arr2 = [1,-1]
    expected = 3
    assert maxAbsValExpr(arr1, arr2) == expected, "Max from val2 case failed"