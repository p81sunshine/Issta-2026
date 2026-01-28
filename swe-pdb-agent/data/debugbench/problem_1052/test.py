from solution import *

def test_case_1x1_grid():
    grid = [[0]]
    root = construct(grid)
    assert root is not None
    assert root.isLeaf is True
    assert root.val == 0

def test_example_1():
    grid = [[0, 1], [1, 0]]
    root = construct(grid)
    assert root is not None
    assert not root.isLeaf
    assert root.val == 0
    assert root.top_left.isLeaf
    assert root.top_left.val == 0
    assert root.top_right.isLeaf
    assert root.top_right.val == 1
    assert root.bottom_left.isLeaf
    assert root.bottom_left.val == 1
    assert root.bottom_right.isLeaf
    assert root.bottom_right.val == 0

def test_4x4_grid():
    grid = [
        [0,1,0,1],
        [1,0,1,0],
        [0,1,0,1],
        [1,0,1,0]
    ]
    root = construct(grid)
    assert root is not None
    assert not root.isLeaf
    assert root.val == 0
    # Check top-left quadrant
    tl = root.top_left
    assert not tl.isLeaf
    assert tl.val == 0

def test_all_same_2x2():
    grid = [[1, 1], [1, 1]]
    root = construct(grid)
    assert root.isLeaf is True
    assert root.val == 1