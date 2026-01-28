from solution import *

def test_example_1():
    assert componentValue([6,2,2,2,6], [[0,1],[1,2],[1,3],[3,4]]) == 2

def test_example_2():
    assert componentValue([2], []) == 0

def test_chain_split():
    assert componentValue([1,1,1], [[0,1],[1,2]]) == 2

def test_no_possible_splits():
    assert componentValue([3,1,3,1,3], [[0,1],[1,2],[2,3],[3,4]]) == 0

def test_two_node_split():
    assert componentValue([3,3], [[0,1]]) == 1