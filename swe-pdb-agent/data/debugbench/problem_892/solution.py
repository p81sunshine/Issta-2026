import random
from typing import List

def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    tree = None
    ans = []
    for i, x in enumerate(nums):
        tree = insert(tree, x)
        if size(tree) > k:
            tree = remove(tree, nums[i - k])
        if size(tree) == k:
            if k % 2 == 1:
                ans.append(get(tree, k // 2 + 1))
            else:
                ans.append((release(tree, k // 2) + get(tree, k // 2 + 1)) / 2)
        return ans

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