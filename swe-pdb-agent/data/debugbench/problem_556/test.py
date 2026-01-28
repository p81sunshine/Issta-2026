from solution import *

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def test_example_1():
    root1 = build_tree([2,1,4])
    root2 = build_tree([1,0,3])
    expected = [0,1,1,2,3,4]
    result = getAllElements(root1, root2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_example_2():
    root1 = build_tree([1, None, 8])
    root2 = build_tree([8, 1])
    expected = [1,1,8,8]
    result = getAllElements(root1, root2)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_edge_case_empty():
    root1 = build_tree([])  # Empty tree
    root2 = build_tree([5])
    expected = [5]
    result = getAllElements(root1, root2)
    assert result == expected, "Failed on empty tree and single node"

def test_edge_case_both_empty():
    root1 = build_tree([])
    root2 = build_tree([])
    expected = []
    result = getAllElements(root1, root2)
    assert result == expected, "Failed when both trees are empty"

def test_edge_case_right_only():
    root1 = build_tree([0, None, 1])
    root2 = build_tree([])
    expected = [0,1]
    result = getAllElements(root1, root2)
    assert result == expected, "Failed on tree with only right children"