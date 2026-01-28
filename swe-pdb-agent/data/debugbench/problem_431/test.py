from solution import *

def test_example_1():
    grid = [[0, 1], [1, 0]]
    root = construct(grid)
    assert root is not None, "Root should not be None"
    assert not root.isLeaf, "Root should not be a leaf"
    assert root.val == 0, "Root's val should be 0"
    assert root.top_left.isLeaf and root.top_left.val == 0
    assert root.top_right.isLeaf and root.top_right.val == 1
    assert root.bottom_left.isLeaf and root.bottom_left.val == 1
    assert root.bottom_right.isLeaf and root.bottom_right.val == 0

def test_1x1_grid():
    grid = [[1]]
    root = construct(grid)
    assert root.isLeaf, "1x1 grid root should be a leaf"
    assert root.val == 1, "1x1 grid root val should be 1"

def test_4x4_all_ones():
    grid = [[1]*4 for _ in range(4)]
    root = construct(grid)
    assert root.isLeaf, "4x4 all-ones grid should produce a single leaf"
    assert root.val == 1, "4x4 all-ones grid leaf val should be 1"
    assert root.top_left is None
    assert root.top_right is None
    assert root.bottom_left is None
    assert root.bottom_right is None

def test_4x4_split():
    grid = [
        [0,0,1,1],
        [0,0,1,1],
        [1,1,0,0],
        [1,1,0,0]
    ]
    root = construct(grid)
    assert not root.isLeaf, "Root should not be a leaf"
    assert root.top_left.isLeaf and root.top_left.val == 0
    assert root.top_right.isLeaf and root.top_right.val == 1
    assert root.bottom_left.isLeaf and root.bottom_left.val == 1
    assert root.bottom_right.isLeaf and root.bottom_right.val == 0