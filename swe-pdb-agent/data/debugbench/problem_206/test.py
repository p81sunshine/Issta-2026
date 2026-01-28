from solution import *

def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def get_in_order(root):
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res

def is_balanced(root):
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    return check(root) != -1

def test_example_1():
    head = create_linked_list([-10, -3, 0, 5, 9])
    root = sortedListToBST(head)
    in_order = get_in_order(root)
    assert in_order == [-10, -3, 0, 5, 9], "In-order traversal mismatch"
    assert is_balanced(root), "Tree is not balanced"

def test_example_2():
    head = create_linked_list([])
    root = sortedListToBST(head)
    assert root is None, "Empty input should return None"

def test_single_element():
    head = create_linked_list([1])
    root = sortedListToBST(head)
    in_order = get_in_order(root)
    assert in_order == [1], "In-order traversal mismatch"
    assert is_balanced(root), "Tree is not balanced"