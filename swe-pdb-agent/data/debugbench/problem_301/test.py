from solution import *

def tree_from_list(lst):
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
        else:
            node.left = None
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        else:
            node.right = None
        i += 1
    return root

def list_from_tree(root):
    if not root:
        return []
    res = []
    curr = root
    while curr:
        res.append(curr.val)
        if curr.right:
            res.append(None)
        curr = curr.right
    return res

def test_example_1():
    input_list = [5,3,6,2,4,None,8,1,None,None,None,7,9]
    expected_output = [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]
    root = tree_from_list(input_list)
    result = increasingBST(root)
    assert list_from_tree(result) == expected_output, "Example 1 failed"

def test_example_2():
    input_list = [5,1,7]
    expected_output = [1, None, 5, None, 7]
    root = tree_from_list(input_list)
    result = increasingBST(root)
    assert list_from_tree(result) == expected_output, "Example 2 failed"

def test_edge_case_single_node():
    input_list = [2]
    expected_output = [2]
    root = tree_from_list(input_list)
    result = increasingBST(root)
    assert list_from_tree(result) == expected_output, "Single node test failed"

def test_edge_case_right_skewed():
    input_list = [1, None, 2, None, 3]
    expected_output = [1, None, 2, None, 3]
    root = tree_from_list(input_list)
    result = increasingBST(root)
    assert list_from_tree(result) == expected_output, "Right skewed test failed"