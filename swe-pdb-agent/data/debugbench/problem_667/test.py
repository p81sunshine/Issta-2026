from solution import *

def test_example_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    expected = [[15,7], [9,20], [3]]
    assert levelOrderBottom(root) == expected, "Test case 1 failed"

def test_example_2():
    root = TreeNode(1)
    expected = [[1]]
    assert levelOrderBottom(root) == expected, "Test case 2 failed"

def test_example_3():
    assert levelOrderBottom(None) is None, "Test case 3 failed"

def test_two_level_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    expected = [[2,3], [1]]
    assert levelOrderBottom(root) == expected, "Two-level tree test failed"

def test_three_level_skewed_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    expected = [[3], [2], [1]]
    assert levelOrderBottom(root) == expected, "Skewed tree test failed"