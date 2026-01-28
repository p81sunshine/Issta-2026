from solution import *

def test_example_1():
    grid = [[0,1],[1,0]]
    root = construct(grid)
    assert root is not None
    assert not root.isLeaf, "Root should not be a leaf node"
    assert root.top_left.isLeaf, "Top-left should be a leaf"
    assert root.top_left.val == 0, "Top-left value should be 0"
    assert root.top_right.isLeaf, "Top-right should be a leaf"
    assert root.top_right.val == 1, "Top-right value should be 1"
    assert root.bottom_left.isLeaf, "Bottom-left should be a leaf"
    assert root.bottom_left.val == 1, "Bottom-left value should be 1"
    assert root.bottom_right.isLeaf, "Bottom-right should be a leaf"
    assert root.bottom_right.val == 0, "Bottom-right value should be 0"

def test_uniform_1x1():
    grid = [[1]]
    root = construct(grid)
    assert root.isLeaf, "1x1 grid should produce a leaf node"
    assert root.val == 1, "1x1 value should be 1"

def test_4x4_quarters():
    grid = [
        [0,0,1,1],
        [0,0,1,1],
        [1,1,0,0],
        [1,1,0,0],
    ]
    root = construct(grid)
    assert not root.isLeaf, "Root should not be a leaf"
    # Check each quadrant
    tl = root.top_left
    tr = root.top_right
    bl = root.bottom_left
    br = root.bottom_right
    assert tl.isLeaf and tl.val == 0, "Top-left quadrant should be 0 leaf"
    assert tr.isLeaf and tr.val == 1, "Top-right quadrant should be 1 leaf"
    assert bl.isLeaf and bl.val == 1, "Bottom-left quadrant should be 1 leaf"
    assert br.isLeaf and br.val == 0, "Bottom-right quadrant should be 0 leaf"

def test_merge_identical_quadrants():
    grid = [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
    ]
    root = construct(grid)
    assert root.isLeaf, "All identical values should merge into single leaf"
    assert root.val == 1, "All identical values should have val 1"