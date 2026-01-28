from solution import *

def test_example_1():
    assert componentValue([6,2,2,2,6], [[0,1],[1,2],[1,3],[3,4]]) == 2

def test_example_2():
    assert componentValue([2], []) == 0

def test_two_nodes_equal():
    assert componentValue([4,4], [[0,1]]) == 1

def test_three_nodes():
    assert componentValue([3,3,3], [[0,1], [0,2]]) == 2

def test_straight_line():
    assert componentValue([1,1,1], [[0,1], [1,2]]) == 2