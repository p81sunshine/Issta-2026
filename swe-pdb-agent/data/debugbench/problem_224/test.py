from solution import *
from typing import Optional

def test_example_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert maxDepth(root) == 3, "Example 1 should return 3"

def test_example_2():
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    assert maxDepth(root) == 2, "Example 2 should return 2"

def test_edge_case_empty():
    assert maxDepth(None) == 0, "Empty tree should return 0"

def test_right_subtree_deeper():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    assert maxDepth(root) == 3, "Right subtree deeper should return 3"

def test_single_node():
    root = TreeNode(5)
    assert maxDepth(root) == 1, "Single node should return 1"