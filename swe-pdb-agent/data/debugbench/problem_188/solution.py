# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

def findBottomLeftValue(root: Optional[TreeNode]) -> int:
    depth = 0
    stack = deque([root])
    d = {}
    a = 0
    while stack:
        lvl = []
        for i in range(len(stack)):
            n = stack.popleft()
            lvl.append(n.val)
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
        return lvl[0]