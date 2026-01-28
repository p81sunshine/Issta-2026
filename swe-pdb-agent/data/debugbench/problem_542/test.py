from solution import *

def test_example_1():
    assert stoneGameVI([1,3], [2,1]) == 1, "Failed for first example case"

def test_example_2():
    assert stoneGameVI([1,2], [3,1]) == 0, "Failed for second example case"

def test_example_3():
    assert stoneGameVI([2,4,3], [1,6,7]) == -1, "Failed for third example case"

def test_single_stone_case():
    assert stoneGameVI([5], [3]) == 1, "Failed for single stone edge case"