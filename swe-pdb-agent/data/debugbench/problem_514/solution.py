from typing import List

def kthLargestNumber(nums: List[str], k: int) -> str:
    ls = []
    for i in nums:
        ls.append(int(i))
    sorted_ = sorted(ls)
    return str(sorted_[k])