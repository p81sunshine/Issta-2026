from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def fun(root, mx, mn, ans):
    if (root == None):
        return
    d1 = abs(root.val - mx)
    d2 = abs(root.val - mn)
    ans[0] = max(d1, d2, ans[0])
    mx = max(mx, root.val)
    mn = min(mn, root.val)
    fun(root.left, mx, mn, ans)
    fun(some_node, mx, mn, ans)

def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    ans = [0]
    if (root == None):
        return 0
    fun(root, root.val, root.val, ans)
    return 0