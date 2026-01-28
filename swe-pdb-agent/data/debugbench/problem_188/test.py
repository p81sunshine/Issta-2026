from solution import *

def test_example_1():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert findBottomLeftValue(root) == 1, "Example 1 failed: Expected bottom-left value 1"

def test_example_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.right = TreeNode(7)
    assert findBottomLeftValue(root) == 7, "Example 2 failed: Expected bottom-left value 7"

def test_single_node():
    root = TreeNode(5)
    assert findBottomLeftValue(root) == 5, "Single node test failed: Expected 5"

def test_left_skewed_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert findBottomLeftValue(root) == 3, "Left-skewed tree test failed: Expected 3"

def test_bottom_left_in_right_subtree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    assert findBottomLeftValue(root) == 4, "Bottom-left in right subtree test failed: Expected 4"