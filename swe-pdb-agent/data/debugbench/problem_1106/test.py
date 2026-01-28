from solution import *

def test_example_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert maxDepth(root) == 3, "Example 1 failed"

def test_example_2():
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    assert maxDepth(root) == 2, "Example 2 failed"

def test_empty_tree():
    assert maxDepth(None) == 0, "Empty tree test failed"

def test_single_node():
    root = TreeNode(5)
    assert maxDepth(root) == 1, "Single node test failed"

def test_root_with_null_children():
    root = TreeNode(1)
    root.left = None
    root.right = None
    assert maxDepth(root) == 1, "Root with null children test failed"