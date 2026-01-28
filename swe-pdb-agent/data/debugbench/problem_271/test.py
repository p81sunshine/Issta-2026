from solution import *

def test_example_1():
    nums = [6,2,2,2,6]
    edges = [[0,1],[1,2],[1,3],[3,4]]
    assert component_value(nums, edges) == 2, "Example 1 failed"

def test_example_2():
    assert component_value([2], []) == 0, "Example 2 failed"

def test_single_node():
    assert component_value([5], []) == 0, "Single node should return 0"

def test_two_nodes_split():
    assert component_value([3,3], [[0,1]]) == 1, "Two nodes with equal values should return 1"

def test_chain_three_nodes():
    assert component_value([3,3,3], [[0,1], [1,2]]) == 2, "Three-node chain with equal values should return 2"