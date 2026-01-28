from solution import *

def test_example_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    expected = [[15,7], [9,20], [3]]
    actual = levelOrderBottom(root)
    assert actual == expected, "Test case 1 failed"

def test_example_2():
    root = TreeNode(1)
    expected = [[1]]
    actual = levelOrderBottom(root)
    assert actual == expected, "Test case 2 failed"

def test_edge_case_empty():
    root = None
    expected = None
    actual = levelOrderBottom(root)
    assert actual == expected, "Test case empty tree failed"

def test_case_missing_children():
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    expected = [[2], [1]]
    actual = levelOrderBottom(root)
    assert actual == expected, "Test case missing children failed"