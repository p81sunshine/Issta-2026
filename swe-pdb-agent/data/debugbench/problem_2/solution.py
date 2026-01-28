from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    ans = []
    def inorder(root, ans):
        if not root:
            return None
        ans.append(root.val)
        inorder(root.left, ans)
        inorder(root.right, ans)
    inorder(root, ans)
    return ans