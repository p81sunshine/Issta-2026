from solution import *

def build_tree_from_list(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    idx = 1
    while queue and idx < len(values):
        node = queue.pop(0)
        if idx < len(values):
            val = values[idx]
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
            idx += 1
        if idx < len(values):
            val = values[idx]
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
            idx += 1
    return root

def test_example_1():
    root = build_tree_from_list([8,3,10,1,6,None,14,None,None,4,7,13])
    assert maxAncestorDiff(root) == 7, "Example 1 should return 7"

def test_example_2():
    root = build_tree_from_list([1,None,2,None,0,3])
    assert maxAncestorDiff(root) == 3, "Example 2 should return 3"

def test_two_node_tree():
    root = build_tree_from_list([2,1])
    assert maxAncestorDiff(root) == 1, "Two-node tree should return 1"

def test_deeper_difference():
    root = build_tree_from_list([5,3,None,None,1])
    assert maxAncestorDiff(root) == 4, "Deeper difference should be 4"

def test_another_edge_case():
    root = build_tree_from_list([10,2,None,1])
    assert maxAncestorDiff(root) == 9, "The max difference between 10 and 1 should be 9"