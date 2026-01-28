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
                ans.append((get(tree, k // 2) + get(tree, k // 2 + 1)) / 2)
    return ans