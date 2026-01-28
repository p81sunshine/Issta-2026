from solution import *

def test_example_1():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert maxDepth(root) == 3, "Example 1 failed"

def test_example_2():
    root = TreeNode(1, None, TreeNode(2))
    assert maxDepth(root) == 2, "Example 2 failed"

def test_empty_tree():
    assert maxDepth(None) == 0, "Empty tree should return 0"

def test_single_node():
    root = TreeNode(5)
    assert maxDepth(root) == 1, "Single node should return 1"

def test_linear_right():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert maxDepth(root) == 3, "Linear right tree failed"