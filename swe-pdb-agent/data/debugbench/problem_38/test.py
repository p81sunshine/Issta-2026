from solution import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    index = 1
    while queue and index < len(values):
        node = queue.pop(0)
        val = values[index]
        index += 1
        if val is not None:
            node.left = TreeNode(val)
            queue.append(node.left)
        else:
            node.left = None
        if index < len(values):
            val = values[index]
            index += 1
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
            else:
                node.right = None
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

def test_both_empty():
    root1 = None
    root2 = None
    expected = []
    result = getAllElements(root1, root2)
    assert result == expected, f"Expected empty list for two null roots"

def test_one_empty():
    root1 = None
    root2 = build_tree([5])
    expected = [5]
    result = getAllElements(root1, root2)
    assert result == expected, f"Expected [5] when one tree is empty"

def test_single_nodes():
    root1 = build_tree([3])
    root2 = build_tree([5])
    expected = [3,5]
    result = getAllElements(root1, root2)
    assert result == expected, f"Expected [3,5] for single-node trees"