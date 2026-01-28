from solution import *

def test_example_1():
    assert stoneGameVI([1,3], [2,1]) == 1, "Example 1 should return 1"

def test_example_2():
    assert stoneGameVI([1,2], [3,1]) == 0, "Example 2 should return 0"

def test_example_3():
    assert stoneGameVI([2,4,3], [1,6,7]) == -1, "Example 3 should return -1"

def test_case_4():
    assert stoneGameVI([5,3,4], [2,4,3]) == 1, "Custom test case should return 1"

def test_single_stone():
    assert stoneGameVI([5], [5]) == 1, "Single stone case should return 1"