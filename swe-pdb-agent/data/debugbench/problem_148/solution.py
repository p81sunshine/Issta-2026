from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    postorder_idx = len(postorder) - 1

    def treeHelper(left, right):
        nonlocal postorder_idx
        if left > right:
            return None

        node_val = postorder[postorder_idx]
        root = TreeNode(node_val)
        postorder_idx -= 1

        inorder_index = inorder_map[node_val]

        root.left = treeHelper(inorder_index + 1, right)
        root.right = treeHelper(left, inorder_index - 1)

        return root

    return treeHelper(0, len(inorder) - 1)