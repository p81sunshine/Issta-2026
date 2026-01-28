from solution import *

def test_example_1():
    assert findMiddleIndex([2,3,-1,8,4]) == 3, "Failed for example 1"

def test_example_2():
    assert findMiddleIndex([1,-1,4]) == 2, "Failed for example 2"

def test_example_3():
    assert findMiddleIndex([2,5]) == -1, "Failed for example 3"

def test_classic_case():
    assert findMiddleIndex([1,7,3,6,5,6]) == 3, "Failed for classic balanced case"