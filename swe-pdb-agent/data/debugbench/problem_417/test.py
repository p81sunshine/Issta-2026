from solution import *

def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

def test_example_1():
    input_list = [3,9,20,None,None,15,7]
    expected = [[15,7],[9,20],[3]]
    root = list_to_tree(input_list)
    assert levelOrderBottom(root) == expected

def test_example_2():
    input_list = [1]
    expected = [[1]]
    root = list_to_tree(input_list)
    assert levelOrderBottom(root) == expected

def test_example_3():
    input_list = []
    expected = None
    root = list_to_tree(input_list)
    assert levelOrderBottom(root) == expected

def test_additional_case():
    input_list = [1,2,None,3]
    expected = [[3],[2],[1]]
    root = list_to_tree(input_list)
    assert levelOrderBottom(root) == expected