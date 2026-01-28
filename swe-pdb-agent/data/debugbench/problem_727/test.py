from solution import *

def test_example_1():
    grid = [[0,1],[1,0]]
    root = construct(grid)
    assert not root.isLeaf, "Root should not be a leaf"
    assert not root.val  # root val should be False (0)
    
    # Check all four children
    assert root.top.isLeaf
    assert not root.top.val  # 0
    
    assert root.right.isLeaf
    assert root.right.val  # 1
    
    assert root.bottom.isLeaf
    assert root.bottom.val  # 1
    
    assert root.left.isLeaf
    assert not root.left.val  # 0

def test_example_2():
    grid = [[1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0]]
    root = construct(grid)
    assert not root.isLeaf, "Root should not be a leaf"
    assert root.val  # root val should be True (1)

    # Check top-right quadrant (which should split further)
    assert not root.right.isLeaf
    assert not root.right.val

def test_1x1_grid():
    grid = [[1]]
    root = construct(grid)
    assert root.isLeaf
    assert root.val

def test_all_same_values():
    grid = [[0,0],[0,0]]
    root = construct(grid)
    assert root.isLeaf
    assert not root.val