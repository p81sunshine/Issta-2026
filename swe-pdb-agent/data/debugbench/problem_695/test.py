from solution import *

def test_example_1():
    grid = [[0, 1], [1, 0]]
    root = construct(grid)
    assert not root.isLeaf, "Root should not be a leaf"
    assert root.val == 0, "Root val should be 0"
    assert root.top_left.isLeaf, "Top left should be a leaf"
    assert root.top_left.val == 0, "Top left val should be 0"
    assert root.top_right.isLeaf, "Top right should be a leaf"
    assert root.top_right.val == 1, "Top right val should be 1"
    assert root.bottom_left.isLeaf, "Bottom left should be a leaf"
    assert root.bottom_left.val == 1, "Bottom left val should be 1"
    assert root.bottom_right.isLeaf, "Bottom right should be a leaf"
    assert root.bottom_right.val == 0, "Bottom right val should be 0"

def test_4x4_all_ones():
    grid = [[1]*4 for _ in range(4)]
    root = construct(grid)
    assert root.isLeaf is True, "Root should be a leaf for all 1s 4x4 grid"
    assert root.val == 1, "Root val should be 1"

def test_1x1_grid():
    grid = [[1]]
    root = construct(grid)
    assert root.isLeaf is True, "1x1 grid should return a leaf node"
    assert root.val == 1, "Value should be 1"