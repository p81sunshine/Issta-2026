from solution import *

def test_example_1():
    grid = [[0, 1], [1, 0]]
    root = construct(grid)
    assert not root.isLeaf, "Root should not be a leaf"
    assert root.val == 0, "Root's value is incorrect"
    
    # Verify four children exist and are leaves
    children = [root.top_left, root.top_right, root.bottom_left, root.bottom_right]
    for child in children:
        assert child.isLeaf, "All four children should be leaves"
    
    assert children[0].val == 0
    assert children[1].val == 1
    assert children[2].val == 1
    assert children[3].val == 0

def test_1x1_grid():
    grid = [[1]]
    root = construct(grid)
    assert root.isLeaf, "1x1 grid should produce a leaf node"
    assert root.val == 1, "1x1 node's value should be 1"
    
    # Verify all pointers are None
    assert root.top_left is None
    assert root.top_right is None
    assert root.bottom_left is None
    assert root.bottom_right is None

def test_4x4_uniform_grid():
    grid = [[1]*4 for _ in range(4)]
    root = construct(grid)
    assert root.isLeaf, "Uniform 4x4 grid should result in a single leaf"
    assert root.val == 1
    
    # Verify all child pointers are None
    assert root.top_left is None
    assert root.top_right is None
    assert root.bottom_left is None
    assert root.bottom_right is None

def test_example_2():
    grid = [
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0]
    ]
    root = construct(grid)
    assert not root.isLeaf, "Root should not be a leaf"
    
    # Verify complex structure doesn't collapse into single leaf
    # Check top_right quadrant is a non-leaf with four children
    top_right = root.top_right
    assert not top_right.isLeaf, "Top-right quadrant should not be a leaf"
    assert all([
        top_right.top_left is not None,
        top_right.top_right is not None,
        top_right.bottom_left is not None,
        top_right.bottom_right is not None
    ])