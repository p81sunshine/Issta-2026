from solution import *

def test_example_1():
    root = TreeNode(5)
    root.left = TreeNode(8)
    root.right = TreeNode(9)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(6)
    assert kthLargestLevelSum(root, 2) == 13, "Example 1 failed"

def test_example_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    assert kthLargestLevelSum(root, 1) == 3, "Example 2 failed"

def test_three_levels_k3():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert kthLargestLevelSum(root, 3) == 1, "Three levels with k=3 failed"

def test_two_levels_k2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert kthLargestLevelSum(root, 2) == 1, "Two levels with k=2 failed"

def test_single_level_k1():
    root = TreeNode(5)
    assert kthLargestLevelSum(root, 1) == 5, "Single level with k=1 failed"