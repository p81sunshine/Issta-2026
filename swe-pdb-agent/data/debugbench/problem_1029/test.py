from solution import *

def test_example_1():
    grid = [[0,1],[1,0]]
    root = construct(grid)
    assert not root.isLeaf
    assert root.top_left.isLeaf
    assert root.top_left.val == 0
    assert root.top_right.isLeaf
    assert root.top_right.val == 1
    assert root.bottom_left.isLeaf
    assert root.bottom_left.val == 1
    assert root.bottom_right.isLeaf
    assert root.bottom_right.val == 0

def test_edge_case_1x1():
    grid = [[1]]
    root = construct(grid)
    assert root.isLeaf
    assert root.val == 1

def test_case_non_leaf_children():
    grid = [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,0]
    ]
    root = construct(grid)
    assert not root.isLeaf
    br = root.bottom_right
    assert not br.isLeaf
    assert br.top_left.isLeaf
    assert br.top_right.isLeaf
    assert br.bottom_left.isLeaf
    assert br.bottom_right.isLeaf
    assert br.top_left.val == 1
    assert br.top_right.val == 1
    assert br.bottom_left.val == 1
    assert br.bottom_right.val == 0