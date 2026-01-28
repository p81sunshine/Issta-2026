from solution import *

def test_example_1():
    arr1 = [1,2,3,4]
    arr2 = [-1,4,5,6]
    assert max_abs_val_expr(arr1, arr2) == 13, "Example 1 failed"

def test_example_2():
    arr1 = [1,-2,-5,0,10]
    arr2 = [0,-2,-1,-7,-4]
    assert max_abs_val_expr(arr1, arr2) == 20, "Example 2 failed"

def test_single_element():
    arr1 = [5]
    arr2 = [3]
    assert max_abs_val_expr(arr1, arr2) == 0, "Single element case failed"

def test_all_zeros():
    arr1 = [0,0,0]
    arr2 = [0,0,0]
    assert max_abs_val_expr(arr1, arr2) == 2, "All zeros case failed"

def test_custom_case():
    arr1 = [1, -1]
    arr2 = [2, -2]
    assert max_abs_val_expr(arr1, arr2) == 7, "Custom case failed"