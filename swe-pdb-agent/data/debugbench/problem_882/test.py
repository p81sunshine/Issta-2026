from solution import *

def test_case_1():
    grid = [[0,1],[1,0]]
    root = construct(grid)
    assert root is not None, "Root should not be None"
    assert not root.isLeaf, "Root should not be a leaf"
    assert root.val == 0, "Root value should be 0"
    
    assert root.top_left.isLeaf, "top_left should be a leaf"
    assert root.top_left.val == 0, "top_left value should be 0"
    
    assert root.top_right.isLeaf, "top_right should be a leaf"
    assert root.top_right.val == 1, "top_right value should be 1"
    
    assert root.bottom_left.isLeaf, "bottom_left should be a leaf"
    assert root.bottom_left.val == 1, "bottom_left value should be 1"
    
    assert root.bottom_right.isLeaf, "bottom_right should be a leaf"
    assert root.bottom_right.val == 0, "bottom_right value should be 0"

def test_all_same_values():
    grid = [[1,1],[1,1]]
    root = construct(grid)
    assert root is not None, "Root should not be None"
    assert root.isLeaf, "Root should be a leaf"
    assert root.val == 1, "Root value should be 1"
    assert root.top_left is None, "Leaf node should have no children"
    assert root.top_right is None, "Leaf node should have no children"
    assert root.bottom_left is None, "Leaf node should have no children"
    assert root.bottom_right is None, "Leaf node should have no children"

def test_single_cell():
    grid = [[1]]
    root = construct(grid)
    assert root is not None, "Root should not be None"
    assert root.isLeaf, "Root should be a leaf"
    assert root.val == 1, "Root value should be 1"
    assert root.top_left is None, "Leaf node should have no children"
    assert root.top_right is None, "Leaf node should have no children"
    assert root.bottom_left is None, "Leaf node should have no children"
    assert root.bottom_right is None, "Leaf node should have no children"