from solution import *

def test_example_1():
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    tree = buildTree(inorder, postorder)
    assert tree.val == 3, "Root value should be 3"
    assert tree.left.val == 9, "Root's left should be 9"
    assert tree.right.val == 20, "Root's right should be 20"
    assert tree.left.left is None, "9's left should be None"
    assert tree.left.right is None, "9's right should be None"
    assert tree.right.left.val == 15, "20's left should be 15"
    assert tree.right.right.val == 7, "20's right should be 7"

def test_example_2():
    inorder = [-1]
    postorder = [-1]
    tree = buildTree(inorder, postorder)
    assert tree.val == -1, "Root value should be -1"
    assert tree.left is None, "Root's left should be None"
    assert tree.right is None, "Root's right should be None"

def test_case_two_nodes():
    inorder = [2, 1]
    postorder = [2, 1]
    tree = buildTree(inorder, postorder)
    assert tree.val == 1, "Root should be 1"
    assert tree.left.val == 2, "Left child should be 2"
    assert tree.right is None, "Right child should be None"

def test_case_three_nodes():
    inorder = [2, 1, 3]
    postorder = [2, 3, 1]
    tree = buildTree(inorder, postorder)
    assert tree.val == 1, "Root should be 1"
    assert tree.left.val == 2, "Left child should be 2"
    assert tree.right.val == 3, "Right child should be 3"
    assert tree.left.left is None
    assert tree.left.right is None
    assert tree.right.left is None
    assert tree.right.right is None