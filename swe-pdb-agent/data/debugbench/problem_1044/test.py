from solution import *

def test_example_1():
    grid = [[0,1],[1,0]]
    root = construct(grid)
    assert not root.isLeaf, "Root should not be a leaf"
    assert root.topLeft.val == 0 and root.topLeft.isLeaf, "Top-left should be leaf 0"
    assert root.topRight.val == 1 and root.topRight.isLeaf, "Top-right should be leaf 1"
    assert root.bottomLeft.val == 1 and root.bottomLeft.isLeaf, "Bottom-left should be leaf 1"
    assert root.bottomRight.val == 0 and root.bottomRight.isLeaf, "Bottom-right should be leaf 0"

def test_merging_case():
    grid = [[1,1],[1,1]]
    root = construct(grid)
    assert root.isLeaf, "Root should be a leaf"
    assert root.val == 1, "Root value should be 1"
    assert root.topLeft is None, "No children expected"

def test_case_3():
    grid = [[1,0],[0,0]]
    root = construct(grid)
    assert not root.isLeaf, "Root should not be a leaf"
    assert root.topLeft.val == 1 and root.topLeft.isLeaf, "Top-left should be leaf 1"
    assert root.topRight.val == 0 and root.topRight.isLeaf, "Top-right should be leaf 0"
    assert root.bottomLeft.val == 0 and root.bottomLeft.isLeaf, "Bottom-left should be leaf 0"
    assert root.bottomRight.val == 0 and root.bottomRight.isLeaf, "Bottom-right should be leaf 0"

def test_4x4_case():
    grid = [[0,0,1,1], [0,0,1,1], [1,1,0,0], [1,1,0,0]]
    root = construct(grid)
    assert not root.isLeaf, "Root should not be a leaf"
    assert root.topLeft.val == 0 and root.topLeft.isLeaf, "Top-left should be leaf 0"
    assert root.topRight.val == 1 and root.topRight.isLeaf, "Top-right should be leaf 1"
    assert root.bottomLeft.val == 1 and root.bottomLeft.isLeaf, "Bottom-left should be leaf 1"
    assert root.bottomRight.val == 0 and root.bottomRight.isLeaf, "Bottom-right should be leaf 0"