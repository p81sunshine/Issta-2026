from typing import List

def findKthPositive(arr: List[int], k: int) -> int:
    l, h = 0, len(arr)
    while l < h:
        mid = (h + l) // 2
        if arr[mid] - mid > k:
            h = mid
        else:
            l = mid + 1
    return l + k - 1