from solution import *

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        val = values[i]
        i += 1
        if val is not None:
            node.left = TreeNode(val)
            queue.append(node.left)
        else:
            node.left = None
        if i < len(values):
            val = values[i]
            i += 1
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
            else:
                node.right = None
    return root

def test_example_1():
    root = build_tree([8,3,10,1,6,None,14,None,None,4,7,13])
    assert maxAncestorDiff(root) == 7, "Example 1 failed"

def test_example_2():
    root = build_tree([1, None, 2, None, 0, 3])
    assert maxAncestorDiff(root) == 3, "Example 2 failed"

def test_single_node():
    root = build_tree([5])
    assert maxAncestorDiff(root) == 0, "Single node test failed"

def test_linear_tree():
    root = build_tree([3,2,None,1])
    assert maxAncestorDiff(root) == 2, "Linear tree test failed"

def test_right_heavy_tree():
    root = build_tree([2, None, 7])
    assert maxAncestorDiff(root) == 5, "Right-heavy tree test failed"