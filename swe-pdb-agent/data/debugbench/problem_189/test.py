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
            left_child = TreeNode(lst[i])
            node.left = left_child
            queue.append(left_child)
        else:
            node.left = None
        i += 1
        if i < len(lst):
            if lst[i] is not None:
                right_child = TreeNode(lst[i])
                node.right = right_child
                queue.append(right_child)
            else:
                node.right = None
        i += 1
    return root

def tree_to_list(root):
    if not root:
        return []
    res = []
    q = [root]
    while q:
        node = q.pop(0)
        if node is None:
            res.append(None)
        else:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
    while res and res[-1] is None:
        res.pop()
    return res

def test_example_1():
    input_list = [5,3,6,2,4,None,8,1,None,None,None,7,9]
    expected_output = [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]
    root = list_to_tree(input_list)
    output_root = increasingBST(root)
    output_list = tree_to_list(output_root)
    assert output_list == expected_output, f"Expected {expected_output}, but got {output_list}"

def test_example_2():
    input_list = [5,1,7]
    expected_output = [1, None, 5, None, 7]
    root = list_to_tree(input_list)
    output_root = increasingBST(root)
    output_list = tree_to_list(output_root)
    assert output_list == expected_output, f"Expected {expected_output}, but got {output_list}"

def test_case_3():
    input_list = [2,1]
    expected_output = [1, None, 2]
    root = list_to_tree(input_list)
    output_root = increasingBST(root)
    output_list = tree_to_list(output_root)
    assert output_list == expected_output, f"Expected {expected_output}, but got {output_list}"

def test_single_node():
    input_list = [10]
    expected_output = [10]
    root = list_to_tree(input_list)
    output_root = increasingBST(root)
    output_list = tree_to_list(output_root)
    assert output_list == expected_output, f"Expected {expected_output}, but got {output_list}"