from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    ans = []
    def inorder(root, ans):
        inorder(root.left, ans)
        ans.append(root.val)
        inorder(root.right, ans)
    inorder(root, ans)
    return ans