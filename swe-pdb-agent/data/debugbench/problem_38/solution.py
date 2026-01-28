from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_all_elements(root1: TreeNode, root2: TreeNode) -> List[int]:
    l = []
    def traversal(root):
        if root is None:
            return
        l.append(root.val)
        traversal(root.left)
        traversal(root.right)
    traversal(root1)
    traversal(root2)
    l.sort()
    return l