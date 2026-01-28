from solution import *

def test_case_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    expected = [[15, 7], [9, 20], [3]]
    result = levelOrderBottom(root)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_case_2():
    root = TreeNode(1)
    expected = [[1]]
    result = levelOrderBottom(root)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_case_3():
    root = None
    expected = []
    result = levelOrderBottom(root)
    assert result == expected, f"Expected {expected}, but got {result}"