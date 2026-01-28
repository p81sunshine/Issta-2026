from solution import *

def test_example_1():
    assert plusOne([1,2,3]) == [1,2,4], "Failed for input [1,2,3]"

def test_example_2():
    assert plusOne([4,3,2,1]) == [4,3,2,2], "Failed for input [4,3,2,1]"

def test_example_3():
    assert plusOne([9]) == [1,0], "Failed for input [9]"

def test_carryover_case():
    assert plusOne([9,9]) == [1,0,0], "Failed for input [9,9]"

def test_partial_carryover():
    assert plusOne([8,9,9]) == [9,0,0], "Failed for input [8,9,9]"