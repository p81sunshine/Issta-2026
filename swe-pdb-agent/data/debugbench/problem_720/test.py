from solution import *

def test_example_1():
    grid = [[0, 1], [1, 0]]
    root = construct(grid)
    assert not root.isLeaf, "Root should not be a leaf in example 1"
    assert root.val == 0, "Root value should be 0"
    assert root.top_left.isLeaf and root.top_left.val == 0
    assert root.top_right.isLeaf and root.top_right.val == 1
    assert root.bottom_left.isLeaf and root.bottom_left.val == 1
    assert root.bottom_right.isLeaf and root.bottom_right.val == 0

def test_all_same_2x2():
    grid = [[1, 1], [1, 1]]
    root = construct(grid)
    assert root.isLeaf, "Root should be a leaf in all same 2x2 grid"
    assert root.val == 1
    assert root.top_left is None
    assert root.top_right is None
    assert root.bottom_left is None
    assert root.bottom_right is None

def test_1x1_grid():
    grid = [[0]]
    root = construct(grid)
    assert root.isLeaf
    assert root.val == 0
    assert root.top_left is None
    assert root.top_right is None
    assert root.bottom_left is None
    assert root.bottom_right is None

def test_empty_grid():
    grid = []
    root = construct(grid)
    assert root is None