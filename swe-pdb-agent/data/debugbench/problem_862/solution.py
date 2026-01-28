from typing import Optional

class ListNode:
    pass

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    currGroup = dummy

    while True:
        kth = get_kth(currGroup, k)
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

        k += 1 

    return dummy.next


def get_kth(node, k):
    while node and k:
        node = node.next
        k -= 1
    return node