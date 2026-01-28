from solution import *

def test_example_1():
    assert component_value([6,2,2,2,6], [[0,1],[1,2],[1,3],[3,4]]) == 2, "Failed for example 1"

def test_example_2():
    assert component_value([2], []) == 0, "Failed for example 2"

def test_two_nodes():
    assert component_value([2, 2], [[0, 1]]) == 1, "Failed for two-node case"

def test_three_nodes_chain():
    assert component_value([1,1,1], [[0,1], [1,2]]) == 2, "Failed for three-node chain"