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
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

def test_example_1():
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    expected = [3,9,20,None,None,15,7]
    assert tree_to_list(buildTree(preorder, inorder)) == expected

def test_example_2():
    preorder = [-1]
    inorder = [-1]
    expected = [-1]
    assert tree_to_list(buildTree(preorder, inorder)) == expected

def test_left_right_mixed():
    preorder = [1,2,3]
    inorder = [2,1,3]
    expected = [1,2,3]
    assert tree_to_list(buildTree(preorder, inorder)) == expected

def test_left_skewed():
    preorder = [4,2,1,3]
    inorder = [1,2,3,4]
    expected = [4,2,None,1,3]
    assert tree_to_list(buildTree(preorder, inorder)) == expected