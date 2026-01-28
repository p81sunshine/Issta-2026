from solution import *

def test_example_1():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = buildTree(preorder, inorder)
    assert root.val == 3
    assert root.left.val == 9
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.val == 20
    assert root.right.left.val == 15
    assert root.right.right.val == 7

def test_example_2():
    preorder = [-1]
    inorder = [-1]
    root = buildTree(preorder, inorder)
    assert root.val == -1
    assert root.left is None
    assert root.right is None

def test_empty_tree():
    preorder = []
    inorder = []
    root = buildTree(preorder, inorder)
    assert root is None

def test_right_skewed_tree():
    preorder = [1, 2, 3]
    inorder = [2, 1, 3]
    root = buildTree(preorder, inorder)
    assert root.val == 1
    assert root.left.val == 2
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.val == 3
    assert root.right.left is None
    assert root.right.right is None