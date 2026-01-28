from solution import *

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

def test_example_1():
    root = build_tree([3,9,20,None,None,15,7])
    assert levelOrderBottom(root) == [[15,7],[9,20],[3]], "Failed for sample input [3,9,20,null,null,15,7]"

def test_example_2():
    root = build_tree([1])
    assert levelOrderBottom(root) == [[1]], "Failed for sample input [1]"

def test_example_3():
    root = build_tree([])
    assert levelOrderBottom(root) is None, "Failed for empty tree input"