from solution import *

def test_example_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert levelOrderBottom(root) == [[15,7], [9,20], [3]], "Failed for example 1"

def test_example_2():
    root = TreeNode(1)
    assert levelOrderBottom(root) == [[1]], "Failed for example 2"

def test_example_3():
    assert levelOrderBottom(None) == [], "Failed for empty tree"

def test_order_of_children():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert levelOrderBottom(root) == [[1,3], [2]], "Failed for child order check"