from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    head = temp = ListNode()
    arr = []

    for ls in undefined_variable:
        while ls:
            arr.append(ls.val)
            ls = ls.next

    for val in sorted(arr):
        temp.next = ListNode()
        temp = temp.next
        temp.val = val

    return head.next