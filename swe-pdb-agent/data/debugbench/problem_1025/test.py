from solution import *

def test_example_1():
    adjacent_pairs = [[2,1],[3,4],[3,2]]
    expected = [1,2,3,4]
    reversed_expected = [4,3,2,1]
    actual = restore_array(adjacent_pairs)
    assert actual in (expected, reversed_expected), "Test case 1 failed"

def test_example_2():
    adjacent_pairs = [[4,-2],[1,4],[-3,1]]
    expected = [-2,4,1,-3]
    reversed_expected = [-3,1,4,-2]
    actual = restore_array(adjacent_pairs)
    assert actual in (expected, reversed_expected), "Test case 2 failed"

def test_example_3():
    adjacent_pairs = [[100000,-100000]]
    expected = [100000, -100000]
    reversed_expected = [-100000, 100000]
    actual = restore_array(adjacent_pairs)
    assert actual in (expected, reversed_expected), "Test case 3 failed"

def test_case_branching():
    adjacent_pairs = [[1,2],[1,3]]
    expected = [2,1,3]
    reversed_expected = [3,1,2]
    actual = restore_array(adjacent_pairs)
    assert actual in (expected, reversed_expected), "Branching test case failed"

def test_case_long_chain():
    adjacent_pairs = [[1,2],[2,3],[3,4],[4,5],[5,6]]
    expected = [1,2,3,4,5,6]
    reversed_expected = [6,5,4,3,2,1]
    actual = restore_array(adjacent_pairs)
    assert actual in (expected, reversed_expected), "Long chain test case failed"