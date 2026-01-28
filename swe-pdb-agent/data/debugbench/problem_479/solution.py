from typing import List

def getLastMoment(n: int, left: List[int], right: List[int]) -> int:
    return max(max(left, default=0), n - max(right, default=n))