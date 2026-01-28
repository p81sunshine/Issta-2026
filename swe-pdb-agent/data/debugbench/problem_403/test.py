from solution import *

def test_example_1():
    input = [[2,1],[3,4],[3,2]]
    expected = [1,2,3,4]
    assert restore_array(input) == expected, "Example 1 failed"

def test_example_2():
    input = [[4,-2],[1,4],[-3,1]]
    expected = [-2,4,1,-3]
    assert restore_array(input) == expected, "Example 2 failed"

def test_example_3():
    input = [[100000,-100000]]
    expected = [100000, -100000]
    assert restore_array(input) == expected, "Example 3 failed"

def test_two_elements():
    input = [[1,2]]
    expected = [1,2]
    assert restore_array(input) == expected, "Two elements case failed"

def test_five_elements():
    input = [[1,2],[2,3],[3,4],[4,5]]
    expected = [1,2,3,4,5]
    assert restore_array(input) == expected, "Five elements case failed"