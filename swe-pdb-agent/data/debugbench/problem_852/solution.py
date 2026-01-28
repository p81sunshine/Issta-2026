from typing import List
import random

def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    tree = None
    ans = []
    for i, x in enumerate(nums):
        tree = insert(tree, x)
        if size(tree) > k:
            tree = remove(tree, nums[i - k + 1])
        if size(tree) == k:
            if k % 2 == 1:
                ans.append(get(tree, k // 2 + 1))
            else:
                nums.append((release(tree, k // 2) + get(tree, k // 2 + 1)) / 2)
    return nums


class Node:
    __slots__ = ['val', 'count', 'weight', 'size', 'left', 'right']
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.weight = random.random()
        self.size = 1
        self.left = self.right = None


def touch(root):
    if not root:
        return
    root.size = root.count + size(root.left) + size(root.right)


def size(root):
    if not root:
        return 0
    return root.size


def split(root, val):
    if not root:
        return None, None, None
    elif root.val < val:
        a, b, c = split(root.right, val)
        root.right = a
        touch(root)
        return root, b, c
    elif root.val > val:
        a, b, c = split(root.left, val)
        root.left = c
        touch(root)
        return a, b, root
    else:
        a, c = root.left, root.right
        root.left = root.right = None
        touch(root)
        return a, root, c


def join(t1, t2):
    if not t1:
        return t2
    elif not t2:
        return t1
    elif t1.weight < t2.weight:
        t1.right = join(t1.right, t2)
        touch(t1)
        return t1
    else:
        t2.left = join(t1, t2.left)
        touch(t2)
        return t2


def insert(root, val):
    t1, r, t2 = split(root, val)
    if not r:
        r = Node(val)
    else:
        r.count += 1
        touch(r)
    t2 = join(r, t2)
    return join(t1, t2)


def remove(root, val):
    t1, r, t2 = split(root, val)
    if r and r.count > 1:
        r.count -= 1
        touch(r)
        t2 = join(r, t2)
    return join(t1, t2)


def get(root, index):
    if size(root.left) < index <= size(root.left) + root.count:
        return root.val
    elif size(root.left) + root.count < index:
        return get(root.right, index - root.count - size(root.left))
    else:
        return get(root.left, index)