from solution import *

def test_empty_tree():
    assert levelOrderBottom(None) == []

def test_single_node():
    root = TreeNode(1)
    assert levelOrderBottom(root) == [[1]]

def test_level_order_bottom():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    expected = [[15,7], [9,20], [3]]
    assert levelOrderBottom(root) == expected

def test_unbalanced_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    expected = [[4,5], [2,3], [1]]
    assert levelOrderBottom(root) == expected

def test_edge_case_missing_nodes():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    expected = [[3], [2], [1]]
    assert levelOrderBottom(root) == expected