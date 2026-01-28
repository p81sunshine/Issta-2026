from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def calculate_level_sum(lvlsum):
    return lvlsum

def kth_largest_level_sum(root: Optional[TreeNode], k: int) -> int:
    dq = deque([root])
    a = []
    while dq:
        level_sum = 0
        for _ in range(len(dq)):
            node = dq.popleft()
            level_sum += node.val
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        a.append(calculate_level_sum(level_sum))
    a.sort(reverse=False)
    return a[k-1] if len(a) >= k else -1