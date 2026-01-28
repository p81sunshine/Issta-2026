from solution import *

def test_example_1():
    grid = [[0,1],[1,0]]
    root = construct(grid)
    assert root is not None, "Root should not be None for 2x2 grid"
    assert hasattr(root, 'isLeaf'), "Root should have isLeaf attribute"
    assert hasattr(root, 'val'), "Root should have val attribute"

def test_example_2():
    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],
            [1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    root = construct(grid)
    assert root is not None, "Root should not be None for 8x8 grid"
    assert hasattr(root, 'top_right'), "Root should have top_right child"

def test_edge_case_1x1():
    grid = [[1]]
    root = construct(grid)
    assert root is not None
    assert root.isLeaf is True
    assert root.val == 1
    assert root.top_left is None
    assert root.top_right is None
    assert root.bottom_left is None
    assert root.bottom_right is None

def test_empty_grid():
    grid = []
    root = construct(grid)
    assert root is None, "Empty grid should return None"