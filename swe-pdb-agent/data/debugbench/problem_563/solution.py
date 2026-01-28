from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tsum(root):
    if root == None:
        return 0
    x = root.val + tsum(root.left) + tsum(root.right)
    return x

def fun(root, sm, mx):
    if root == None:
        return 0
    a = fun(root.left, sm, mx)
    b = fun(root.right, sm, mx)
    mx[0] = max(mx[0], a * sm, b * (sm - b))
    return a + b + root.val

def maxProduct(root: Optional[TreeNode]) -> int:
    mx = [0]
    sm = tsum(root)
    memo = {}
    fun(root, sm, mx)
    return mx[0] % (10**9 )