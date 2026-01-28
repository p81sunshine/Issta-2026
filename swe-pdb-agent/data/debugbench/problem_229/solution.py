from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthLargestLevelSum(root: Optional[TreeNode], k: int) -> int:
    dq = deque([root])
    a = []
    lvl = 1
    while dq:
        lvlsum = 0
        for i in range(len(dq)):
            n = dq.popleft()
            lvlsum += n.val
            if n.left: dq.append(n.left)
            if n.right: dq.append(n.right)
                
        a.append(calculateLevelSum(lvlsum)) 
        lvl += 1
    a.sort(reverse=False)
    return a[k] if len(a) >= k else -1