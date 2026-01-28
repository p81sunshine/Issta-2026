from solution import *

def test_example_1():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    expected = [[15,7], [9,20], [3]]
    assert levelOrderBottom(root) == expected, "Failed for example 1"

def test_example_2():
    root = TreeNode(1)
    expected = [[1]]
    assert levelOrderBottom(root) == expected, "Failed for example 2"

def test_example_3():
    assert levelOrderBottom(None) == [], "Failed for example 3"

def test_additional_case():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    expected = [[2,3], [1]]
    assert levelOrderBottom(root) == expected, "Failed for additional case"