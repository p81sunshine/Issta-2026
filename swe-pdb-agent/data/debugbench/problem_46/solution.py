from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

    l = []
    length = 0
    ptr = head
    while ptr:
        length += 1
        ptr = ptr.next

    arrange = []
    maxi = length // k 
    remain = length % k

    for i in range(k):
        if remain:
            arrange.append(maxi )  
            remain -= 1
        else:
            arrange.append(maxi)

    j = 0
    ptr = head 
    i = 0
    while ptr:
        q = ptr 
        i += 1
        ptr = ptr.next 
        if i == arrange[j]:
            l.append(head)
            head = ptr 
            i = 0
            j += 1

    for i in range(j, k):
        l.append(None)
    return l