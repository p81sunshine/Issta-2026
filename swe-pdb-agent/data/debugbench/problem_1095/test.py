from solution import *
import pytest

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values: list) -> TreeNode:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        if i < len(values):
            left_val = values[i]
            if left_val is not None:
                current.left = TreeNode(left_val)
                queue.append(current.left)
            i += 1
        if i < len(values):
            right_val = values[i]
            if right_val is not None:
                current.right = TreeNode(right_val)
                queue.append(current.right)
            i += 1
    return root

def test_example_1():
    root = build_tree([0,1,2,3,4,3,4])
    assert smallest_from_leaf(root) == "dba", "Test case 1 failed"

def test_example_2():
    root = build_tree([25,1,3,1,3,0,2])
    assert smallest_from_leaf(root) == "adz", "Test case 2 failed"

def test_example_3():
    root = build_tree([2,2,1,None,1,0,None,0])
    assert smallest_from_leaf(root) == "abc", "Test case 3 failed"

def test_single_node():
    root = build_tree([0])
    assert smallest_from_leaf(root) == "a", "Single node test failed"

def test_two_node_left():
    root = build_tree([0, 1])
    assert smallest_from_leaf(root) == "ba", "Two node left test failed"

def test_left_right_min():
    root = build_tree([0, 25, 0])
    assert smallest_from_leaf(root) == "aa", "Left-right min test failed"