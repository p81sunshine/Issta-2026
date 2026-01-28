from solution import *
import pytest
from collections import deque

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    idx = 1
    while q and idx < len(values):
        node = q.popleft()
        if values[idx] is not None:
            node.left = TreeNode(values[idx])
            q.append(node.left)
        idx += 1
        if idx < len(values) and values[idx] is not None:
            node.right = TreeNode(values[idx])
            q.append(node.right)
        idx += 1
    return root

def test_example_1():
    root = build_tree([5,8,9,2,1,3,7,4,6])
    assert kthLargestLevelSum(root, 2) == 13

def test_example_2():
    root = build_tree([1,2,None,3])
    assert kthLargestLevelSum(root, 1) == 3

def test_sort_order_case():
    root = build_tree([1, 0, 3, None, None, 2, 0])
    assert kthLargestLevelSum(root, 2) == 2

def test_k_larger_than_levels():
    root = build_tree([1,2,3])
    assert kthLargestLevelSum(root, 3) == -1