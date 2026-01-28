from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    a = b = head
    while a != None and a.next != None:
        b = b.next
        a = a.next
        if a == b:
            return True
    return False