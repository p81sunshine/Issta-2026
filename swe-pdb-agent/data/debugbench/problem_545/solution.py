from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: Optional['ListNode'], k: int) -> Optional['ListNode']:
    dummy = ListNode(0, head)
    currGroup = dummy

    while True:
        kth = getKth(currGroup, k)
        if not kth:
            break
        nextGroup = kth.next

        # reverse the currGroup
        prev, curr = kth.next, nextGroup
        while curr != nextGroup:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        currGroup.next, currGroup = kth, currGroup.next

    return dummy.next

def getKth(node: Optional['ListNode'], k: int) -> Optional['ListNode']:
    while node and k:
        node = node.next
        k -= 1
    return node