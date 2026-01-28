from solution import *

def build_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        current = queue.pop(0)
        if i < len(lst):
            if lst[i] is not None:
                current.left = TreeNode(lst[i])
                queue.append(current.left)
            else:
                current.left = None
            i += 1
        if i < len(lst):
            if lst[i] is not None:
                current.right = TreeNode(lst[i])
                queue.append(current.right)
            else:
                current.right = None
            i += 1
    return root

def test_example_1():
    input_str = 'Input: root = [3,9,20,null,null,15,7]\nOutput: [[15,7],[9,20],[3]]'
    root_list_str = input_str.split('root = ')[1].split('\n')[0].strip()
    root_list = eval(root_list_str.replace('null', 'None'))
    root = build_tree(root_list)
    expected = [[15, 7], [9, 20], [3]]
    actual = levelOrderBottom(root)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_example_2():
    input_str = 'Input: root = [1]\nOutput: [[1]]'
    root_list_str = input_str.split('root = ')[1].split('\n')[0].strip()
    root_list = eval(root_list_str.replace('null', 'None'))
    root = build_tree(root_list)
    expected = [[1]]
    actual = levelOrderBottom(root)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_example_3():
    input_str = 'Input: root = []\nOutput: []'
    root_list_str = input_str.split('root = ')[1].split('\n')[0].strip()
    root_list = eval(root_list_str.replace('null', 'None'))
    root = build_tree(root_list)
    expected = None
    actual = levelOrderBottom(root)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_additional_case():
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    expected = [[4, 5, 6, 7], [2, 3], [1]]
    actual = levelOrderBottom(root)
    assert actual == expected, f"Expected {expected}, but got {actual}"