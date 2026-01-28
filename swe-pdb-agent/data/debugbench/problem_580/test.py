from solution import *

def test_example_1():
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    expected = [1, 3, 2]
    assert inorderTraversal(root) == expected, "Test case 1 failed"

def test_example_2():
    root = None
    expected = []
    assert inorderTraversal(root) == expected, "Test case 2 failed"

def test_example_3():
    root = TreeNode(1)
    expected = [1]
    assert inorderTraversal(root) == expected, "Test case 3 failed"

def test_full_binary_tree():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    expected = [1, 2, 3]
    assert inorderTraversal(root) == expected, "Full binary tree test failed"

def test_left_skewed_tree():
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    expected = [1, 2, 3]
    assert inorderTraversal(root) == expected, "Left skewed tree test failed"