from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_bottom(root: Optional[TreeNode]) -> List[List[int]]:
    def check_reverse(ans):
        l, r = 0, len(ans) - 1
        while l <= r:
            ans[l], ans[r] = ans[r], ans[l]
            l += 1
        r -= 1
        return ans

    if not root:
        return None
    q, ans = [root], []
    while q:
        n, l = len(q), []
        for i in range(n):
            curr = q.pop(0)
            l.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        ans.append(l)
    return check_reverse(ans)