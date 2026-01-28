from solution import *
from typing import Optional, List, Any

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(lst: List[Any]) -> Optional[TreeNode]:
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root

def test_example_1():
    root = build_tree_from_list([3,9,20,None,None,15,7])
    expected = [[15,7],[9,20],[3]]
    result = level_order_bottom(root)
    assert result == expected, f"Expected {expected} but got {result}"

def test_example_2():
    root = build_tree_from_list([1])
    expected = [[1]]
    result = level_order_bottom(root)
    assert result == expected, f"Expected {expected} but got {result}"

def test_example_3():
    root = build_tree_from_list([])
    expected = None
    result = level_order_bottom(root)
    assert result == expected, f"Expected {expected} but got {result}"

def test_edge_case_two_levels():
    root = build_tree_from_list([1,2])
    expected = [[2], [1]]
    result = level_order_bottom(root)
    assert result == expected, f"Expected {expected} but got {result}"