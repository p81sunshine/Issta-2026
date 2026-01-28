from solution import *

def test_example_1():
    grid = [[0, 1], [1, 0]]
    result = construct(grid)
    assert result is not None, "Should construct tree without IndexError"

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
    result = construct(grid)
    assert result is not None, "Should construct tree without IndexError"

def test_1x1_grid():
    grid = [[0]]
    result = construct(grid)
    assert result is not None, "Should construct single-node tree"
    assert result.isLeaf is True, "Root node should be a leaf"
    assert result.val == 0, "Leaf node should have correct value"

def test_4x4_grid():
    grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]
    result = construct(grid)
    assert result is not None, "Should construct tree without IndexError"