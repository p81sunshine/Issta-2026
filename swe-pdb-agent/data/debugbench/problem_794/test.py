from solution import *

def test_example_1():
    grid = [[0,1],[1,0]]
    root = construct(grid)
    assert root is not None, "Root should not be None"
    assert not root.isLeaf, "Root should not be a leaf"
    assert root.val == 0, "Root value should be 0"
    assert root.top_left.isLeaf is True, "Top left should be a leaf"
    assert root.top_left.val == 0, "Top left value should be 0"
    assert root.top_right.isLeaf is True, "Top right should be a leaf"
    assert root.top_right.val == 1, "Top right value should be 1"
    assert root.bottom_left.isLeaf is True, "Bottom left should be a leaf"
    assert root.bottom_left.val == 1, "Bottom left value should be 1"
    assert root.bottom_right.isLeaf is True, "Bottom right should be a leaf"
    assert root.bottom_right.val == 0, "Bottom right value should be 0"

def test_example_2():
    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    root = construct(grid)
    assert root is not None, "Root should not be None"
    assert not root.isLeaf, "Root should not be a leaf"

def test_edge_case_1x1():
    grid = [[1]]
    root = construct(grid)
    assert root.isLeaf is True, "Root should be a leaf"
    assert root.val == 1, "Root value should be 1"

def test_edge_case_2x2_all_ones():
    grid = [[1,1],[1,1]]
    root = construct(grid)
    assert root.isLeaf is True, "Root should be a leaf"
    assert root.val == 1, "Root value should be 1"

def test_edge_case_2x2_mixed():
    grid = [[0,1],[0,1]]
    root = construct(grid)
    assert root is not None, "Root should not be None"
    assert not root.isLeaf, "Root should not be a leaf"
    assert root.val == 0, "Root value should be 0"
    assert root.top_left.isLeaf and root.top_left.val == 0
    assert root.top_right.isLeaf and root.top_right.val == 1
    assert root.bottom_left.isLeaf and root.bottom_left.val == 0
    assert root.bottom_right.isLeaf and root.bottom_right.val == 1