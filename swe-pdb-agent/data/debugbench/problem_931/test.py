from solution import *
import pytest

def test_example_1():
    assert countMaxOrSubsets([3, 1]) == 2, "Example 1 failed"

def test_example_2():
    assert countMaxOrSubsets([2, 2, 2]) == 7, "Example 2 failed"

def test_example_3():
    assert countMaxOrSubsets([3, 2, 1, 5]) == 6, "Example 3 failed"

def test_single_element():
    assert countMaxOrSubsets([5]) == 1, "Single element case failed"

def test_two_zeros():
    assert countMaxOrSubsets([0, 0]) == 3, "Two zeros case failed"