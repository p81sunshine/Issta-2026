from solution import *

def build_tree_from_list(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            else:
                current.left = None
            i += 1
        if i < len(values):
            if values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            else:
                current.right = None
            i += 1
    return root

def test_example_1():
    root = build_tree_from_list([8,3,10,1,6,None,14,None,None,4,7,13])
    assert maxAncestorDiff(root) == 7, "Example 1 failed"

def test_example_2():
    root = build_tree_from_list([1,None,2,None,0,3])
    assert maxAncestorDiff(root) == 3, "Example 2 failed"

def test_edge_single_node():
    root = build_tree_from_list([5])
    assert maxAncestorDiff(root) == 0, "Single node test failed"

def test_edge_two_nodes_left():
    root = build_tree_from_list([2,1])
    assert maxAncestorDiff(root) == 1, "Left child test failed"

def test_edge_two_nodes_right():
    root = build_tree_from_list([2,None,3])
    assert maxAncestorDiff(root) == 1, "Right child test failed"