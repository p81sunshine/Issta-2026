from solution import *

def test_example_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    expected = [[15,7], [9,20], [3]]
    assert levelOrderBottom(root) == expected, "Example 1 failed"

def test_example_2():
    root = TreeNode(1)
    expected = [[1]]
    assert levelOrderBottom(root) == expected, "Example 2 failed"

def test_empty_tree():
    assert levelOrderBottom(None) is None, "Empty tree case failed"

def test_single_left_child():
    root = TreeNode(1)
    root.left = TreeNode(2)
    expected = [[2], [1]]
    assert levelOrderBottom(root) == expected, "Single left child case failed"

def test_single_right_child():
    root = TreeNode(1)
    root.right = TreeNode(2)
    expected = [[2], [1]]
    assert levelOrderBottom(root) == expected, "Single right child case failed"