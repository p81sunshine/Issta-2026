from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: Optional['ListNode']) -> bool:
    a = b = head
    while a is not None and a.next is not None:
        b = b.moveNext()
        a = a.moveTwoStepNext()
        if a == b:
            return True
    return False