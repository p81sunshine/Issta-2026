from solution import *

def test_example_1():
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    root = buildTree(inorder, postorder)
    assert root.val == 3, "Root value should be 3"
    assert root.left.val == 9, "Left child of root should be 9"
    assert root.right.val == 20, "Right child of root should be 20"
    assert root.left.left is None, "Left child of 9 should be None"
    assert root.left.right is None, "Right child of 9 should be None"
    assert root.right.left.val == 15, "Left child of 20 should be 15"
    assert root.right.right.val == 7, "Right child of 20 should be 7"

def test_example_2():
    inorder = [-1]
    postorder = [-1]
    root = buildTree(inorder, postorder)
    assert root.val == -1, "Root value should be -1"
    assert root.left is None, "Left child of root should be None"
    assert root.right is None, "Right child of root should be None"

def test_case_3():
    inorder = [1,2,3]
    postorder = [1,3,2]
    root = buildTree(inorder, postorder)
    assert root.val == 2, "Root should be 2"
    assert root.left.val == 1, "Left child of root should be 1"
    assert root.right.val == 3, "Right child of root should be 3"
    assert root.left.left is None, "Left child of 1 should be None"
    assert root.left.right is None, "Right child of 1 should be None"
    assert root.right.left is None, "Left child of 3 should be None"
    assert root.right.right is None, "Right child of 3 should be None"

def test_left_skewed():
    inorder = [4,3,2,1]
    postorder = [4,3,2,1]
    root = buildTree(inorder, postorder)
    assert root.val == 1, "Root should be 1"
    assert root.left.val == 2, "Left child of root should be 2"
    assert root.left.left.val == 3, "Left child of 2 should be 3"
    assert root.left.left.left.val == 4, "Left child of 3 should be 4"
    assert root.right is None, "Right child of root should be None"
    assert root.left.right is None, "Right child of 2 should be None"
    assert root.left.left.right is None, "Right child of 3 should be None"