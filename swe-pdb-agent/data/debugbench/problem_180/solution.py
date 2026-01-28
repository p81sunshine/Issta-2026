from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    result = ListNode(0)
    result.next = head
    cur = result
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        cur = cur.next
    return result.next