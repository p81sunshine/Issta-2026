from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head: Optional[ListNode]) -> Optional[TreeNode]:
    nums = []
    curr = head
    while curr:
        nums.append(curr.val)
        curr = curr.next
    
    def helper(l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = helper(l, mid)
        root.right = helper(mid + 1, r)
        return root
    
    return helper(0, len(nums) - 1)