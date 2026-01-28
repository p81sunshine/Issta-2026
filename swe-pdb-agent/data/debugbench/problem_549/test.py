from solution import *

def test_example_1():
    assert count_max_or_subsets([3, 1]) == 2

def test_example_2():
    assert count_max_or_subsets([2, 2, 2]) == 7

def test_example_3():
    assert count_max_or_subsets([3, 2, 1, 5]) == 6

def test_single_element():
    assert count_max_or_subsets([5]) == 1

def test_all_zero_elements():
    assert count_max_or_subsets([0, 0, 0]) == 7