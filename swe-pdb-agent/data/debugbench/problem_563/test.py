from solution import *

def list_to_treenode(lst):
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
        if i < len(lst):
            if lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            else:
                node.right = None
            i += 1
        else:
            break
    return root

def test_example_1():
    root = list_to_treenode([1,2,3,4,5,6])
    expected = 110
    assert maxProduct(root) == expected, f"Expected {expected}, got {maxProduct(root)}"

def test_example_2():
    root = list_to_treenode([1, None, 2, 3, 4, None, None, 5, 6])
    expected = 90
    assert maxProduct(root) == expected, f"Expected {expected}, got {maxProduct(root)}"

def test_two_nodes():
    root = list_to_treenode([1, 2])
    expected = 2
    assert maxProduct(root) == expected, f"Expected {expected}, got {maxProduct(root)}"

def test_three_nodes():
    root = list_to_treenode([1,2,3])
    expected = 9
    assert maxProduct(root) == expected, f"Expected {expected}, got {maxProduct(root)}"

def test_complete_tree():
    root = list_to_treenode([4,2,6,1,3,5,7])
    expected = 180
    assert maxProduct(root) == expected, f"Expected {expected}, got {maxProduct(root)}"