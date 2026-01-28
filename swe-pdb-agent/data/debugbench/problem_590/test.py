from solution import *

def test_example_1():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    expected = [2]
    actual = findMode(root)
    assert sorted(actual) == sorted(expected), "Test case 1 failed"

def test_example_2():
    root = TreeNode(0)
    expected = [0]
    actual = findMode(root)
    assert sorted(actual) == sorted(expected), "Test case 2 failed"

def test_multiple_modes():
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(2)
    expected = [1, 2]
    actual = findMode(root)
    assert sorted(actual) == sorted(expected), "Multiple modes test failed"

def test_all_same_values():
    root = TreeNode(5)
    root.left = TreeNode(5)
    root.right = TreeNode(5)
    expected = [5]
    actual = findMode(root)
    assert sorted(actual) == sorted(expected), "All same values test failed"

def test_single_mode_in_deep_tree():
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(1)
    expected = [1]
    actual = findMode(root)
    assert sorted(actual) == sorted(expected), "Single deep mode test failed"