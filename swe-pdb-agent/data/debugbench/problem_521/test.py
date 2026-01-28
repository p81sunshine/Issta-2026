from solution import *
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

def test_example_1():
    root = build_tree([1,5,3,None,4,10,6,9,2])
    start = 3
    assert amountOfTime(root, start) == 4, "Test case 1 failed"

def test_example_2():
    root = build_tree([1])
    start = 1
    assert amountOfTime(root, start) == 0, "Test case 2 failed"

def test_edge_case_chain():
    root = build_tree([2,1,3,None,None,4])
    start = 2
    assert amountOfTime(root, start) == 2, "Chain test case failed"

def test_edge_case_leaf_node():
    root = build_tree([1,2,3,4,5])
    start = 4
    assert amountOfTime(root, start) == 3, "Leaf node test case failed"

def test_edge_case_two_nodes():
    root = build_tree([1,2])
    start = 1
    assert amountOfTime(root, start) == 1, "Two nodes test case failed"

def test_edge_case_start_at_middle():
    root = build_tree([1,2,3,4,5,6,7])
    start = 2
    assert amountOfTime(root, start) == 2, "Start at middle test case failed"
