from solution import *

def test_example_1():
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(14)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right.left = TreeNode(13)
    assert maxAncestorDiff(root) == 7, "Example 1 failed"

def test_example_2():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.left.right = TreeNode(3)
    assert maxAncestorDiff(root) == 3, "Example 2 failed"

def test_two_nodes():
    root = TreeNode(2)
    root.left = TreeNode(1)
    assert maxAncestorDiff(root) == 1, "Two nodes test failed"

def test_straight_line():
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    assert maxAncestorDiff(root) == 2, "Straight line test failed"

def test_deeper_diff():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    assert maxAncestorDiff(root) == 4, "Deeper difference test failed"