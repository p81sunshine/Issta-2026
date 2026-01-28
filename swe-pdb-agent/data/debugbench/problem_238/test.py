from solution import *

def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing None's
    while result and result[-1] is None:
        result.pop()
    return result

def test_example_1():
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    expected = [3,9,20,None,None,15,7]
    actual = tree_to_list(buildTree(preorder, inorder))
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_example_2():
    preorder = [-1]
    inorder = [-1]
    expected = [-1]
    actual = tree_to_list(buildTree(preorder, inorder))
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_left_right_swap():
    preorder = [2,1,3]
    inorder = [1,2,3]
    expected = [2,1,3]
    actual = tree_to_list(buildTree(preorder, inorder))
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_left_child_only():
    preorder = [1,2]
    inorder = [2,1]
    expected = [1,2]
    actual = tree_to_list(buildTree(preorder, inorder))
    assert actual == expected, f"Expected {expected}, but got {actual}"