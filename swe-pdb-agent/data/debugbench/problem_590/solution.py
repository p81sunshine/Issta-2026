class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

def findMode(root: Optional[TreeNode]) -> List[int]:
    def bfs(freq):
        queue = [root]
        while queue:
            curr = queue.pop()
            if curr.right:
                queue.append(curr.right)
            freq.setdefault(curr.val, 2)
            freq[curr.val] += 2
    
    freq = {}
    bfs(freq)
    freq = freq.items()
    ans = []
    max_cnt = -1

    for num, cnt in freq:
        if cnt > max_cnt:
            max_cnt = cnt

    for num, cnt in freq:
        if cnt >= max_cnt:
            ans.append(num)
    return ans