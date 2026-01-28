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

def isSame(head, root):
    if head is None:
        return True
    if root is None:
        return False

    if head.val == root.val:
        return isSame(head.next, root.left) 
        
    return False

def isSubPath(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

    if head.val == root.val:
        if isSame(head, root):
            return True
            
    return isSubPath(head, root.left) or isSubPath(head, root.right)