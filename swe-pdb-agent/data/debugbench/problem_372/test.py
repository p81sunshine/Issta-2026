from solution import *

def test_example_1():
    assert countMaxOrSubsets([3, 1]) == 2

def test_example_2():
    assert countMaxOrSubsets([2, 2, 2]) == 7

def test_example_3():
    assert countMaxOrSubsets([3, 2, 1, 5]) == 6

def test_duplicate_elements():
    assert countMaxOrSubsets([1, 1]) == 3